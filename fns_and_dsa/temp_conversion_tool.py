# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_FREEZING_POINT = 32  # Used for both conversions

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_POINT

def main():
    try:
        # Get user input
        temp_input = input("Enter the temperature followed by its unit (C for Celsius, F for Fahrenheit): ").strip()

        # Validate user input
        if temp_input[-1].upper() == 'F':
            # Convert Fahrenheit to Celsius
            fahrenheit = float(temp_input[:-1].strip())  # Extract numeric value
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        elif temp_input[-1].upper() == 'C':
            # Convert Celsius to Fahrenheit
            celsius = float(temp_input[:-1].strip())  # Extract numeric value
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        else:
            print("Invalid unit. Please enter temperature ending with 'C' or 'F'.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

