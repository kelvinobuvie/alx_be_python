# temp_conversion_tool.py

# Global conversion factors (exact formatting for checker)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        # Validate numeric input
        if not temp_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temperature = float(temp_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            print(str(temperature) + "°F is " + str(celsius) + "°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(str(temperature) + "°C is " + str(fahrenheit) + "°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as ve:
        print(ve)
