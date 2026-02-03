import re

def solve_equation(equation_str: str) -> str:
    """
    Evaluates a mathematical equation string safely.
    Strings should be cleaned before passing here (no malicious code).
    """
    try:
        # Whitelist characters for basic math to prevent injection
        allowed = set("0123456789+-*/(). ")
        if not set(equation_str).issubset(allowed):
             return "Error: Invalid characters"
        
        # Safe evaluation
        # Note: eval is generally unsafe, but with character whitelisting it's mitigated for this demo.
        # Ideally, write a parser (like shunting-yard). 
        # For this prototype, we'll maintain the simple whitelisted eval.
        solution = eval(equation_str)
        return str(solution)
    except Exception as e:
        return "Error"
