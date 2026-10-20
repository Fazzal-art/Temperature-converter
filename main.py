# Temperature Converter
# It converts a temperature from Celsius to Fahrenheit and kelvin

# A small program for practising Git and GitHub.
# How to run it:  python temperature_converter.py

# Ask the user for a temperature in Celsius
celsius = float(input("Temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32
# Convert to kelvin
kelvin = celsius + 273

# Show the result
print("Temperature in Fahrenheit:", fahrenheit)