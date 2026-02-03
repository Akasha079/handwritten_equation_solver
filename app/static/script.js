const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');
const clearBtn = document.getElementById('clearBtn');
const solveBtn = document.getElementById('solveBtn');
const statusText = document.getElementById('statusText');
const resultArea = document.getElementById('resultArea');
const equationDisplay = document.getElementById('equationDisplay');
const solutionDisplay = document.getElementById('solutionDisplay');
const confidenceBar = document.getElementById('confidenceBar');

let isDrawing = false;
let lastX = 0;
let lastY = 0;

// Setup Canvas Resolution for high DPI displays
function resizeCanvas() {
    const parent = canvas.parentElement;
    const rect = parent.getBoundingClientRect();
    canvas.width = rect.width;
    canvas.height = 300; // Fixed height in CSS

    // Fill with white background initially (since we save as image)
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.lineWidth = 4; // Thickness
    ctx.strokeStyle = 'black'; // Drawing color
}

window.addEventListener('resize', resizeCanvas);
resizeCanvas();

// Drawing Functions
function startDrawing(e) {
    isDrawing = true;
    [lastX, lastY] = getCoordinates(e);
    statusText.textContent = "Drawing...";
}

function stopDrawing() {
    isDrawing = false;
    ctx.beginPath();
    statusText.textContent = "Ready to solve";
}

function draw(e) {
    if (!isDrawing) return;
    e.preventDefault();

    const [x, y] = getCoordinates(e);

    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(x, y);
    ctx.stroke();

    [lastX, lastY] = [x, y];
}

function getCoordinates(e) {
    const rect = canvas.getBoundingClientRect();
    let clientX, clientY;

    if (e.type.includes('touch')) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
    } else {
        clientX = e.clientX;
        clientY = e.clientY;
    }

    return [clientX - rect.left, clientY - rect.top];
}

// Event Listeners
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

canvas.addEventListener('touchstart', startDrawing);
canvas.addEventListener('touchmove', draw);
canvas.addEventListener('touchend', stopDrawing);

clearBtn.addEventListener('click', () => {
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    statusText.textContent = "Canvas Cleared";
    resultArea.classList.remove('active');
    setTimeout(() => statusText.textContent = "Ready to draw", 1500);
});

solveBtn.addEventListener('click', async () => {
    // Show loading state
    solveBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Processing...';
    solveBtn.disabled = true;

    const dataURL = canvas.toDataURL('image/png');

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: dataURL })
        });

        const data = await response.json();

        // Update UI
        equationDisplay.textContent = data.equation || "?";
        solutionDisplay.textContent = data.solution;

        // Animate confidence bar
        const confidencePercent = Math.round(data.confidence * 100);
        confidenceBar.style.width = `${confidencePercent}%`;

        resultArea.classList.add('active');
        statusText.textContent = "Solved!";

    } catch (error) {
        console.error('Error:', error);
        statusText.textContent = "Error occurred";
        equationDisplay.textContent = "Error";
        solutionDisplay.textContent = "---";
    } finally {
        solveBtn.innerHTML = '<span>Solve Equation</span><i class="fa-solid fa-wand-magic-sparkles"></i>';
        solveBtn.disabled = false;
    }
});
