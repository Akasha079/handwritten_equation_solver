import sympy as sp

def solve_equation(equation: str):
    try:
        result = sp.sympify(equation)
        return str(result)
    except Exception as e:
        return f"Error solving equation: {str(e)}"
