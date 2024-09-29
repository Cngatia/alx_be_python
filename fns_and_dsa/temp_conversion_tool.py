# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    # Formula: Celsius * (9/5) + 32
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    try:
        temp_input = input("Enter the temperature to convert(e.g., 100F or 37C): ").strip()
        
        if temp_input[-1].upper() == 'F':
            fahrenheit = float(temp_input[:-1])
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C.")
        
        elif temp_input[-1].upper() == 'C':
            celsius = float(temp_input[:-1])
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F.")
        
        else:
            raise ValueError("Invalid temperature unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(f"Error: {e} Please enter a valid numeric temperature.")

if __name__ == "__main__":
    main()
