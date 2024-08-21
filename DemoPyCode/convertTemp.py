# GSH 7/24/24 -This code takes a temperature as input from the user and converts it.
# Example: enter 70F it will convert to C, or enter 20C it will convert to F.
#
#
def convert_temperature(temp_input):
    try:
        if temp_input[-1].upper() == 'C':
            # Convert from Celsius to Fahrenheit
            celsius = float(temp_input[:-1])
            fahrenheit = (celsius * 9/5) + 32
            return f"{celsius}C is {fahrenheit:.2f}F"
        elif temp_input[-1].upper() == 'F':
            # Convert from Fahrenheit to Celsius
            fahrenheit = float(temp_input[:-1])
            celsius = (fahrenheit - 32) * 5/9
            return f"{fahrenheit}F is {celsius:.2f}C"
        else:
            return "Invalid input format. Please enter a temperature followed by 'C' or 'F'."
    except ValueError:
        return "Invalid number. Please enter a valid temperature."

# Get user input
user_input = input("Enter a temperature (e.g., 22C or 72F): ")
# Print the conversion result
print(convert_temperature(user_input))