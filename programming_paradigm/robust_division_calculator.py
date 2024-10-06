# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform division
        result = num / denom
        return f"The result is: {result}"
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    except ValueError:
        return "Error: Please provide numeric values for numerator and denominator."
