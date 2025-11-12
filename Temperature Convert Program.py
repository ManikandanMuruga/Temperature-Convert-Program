# Task 3: Temperature Converter
# This program converts temperatures between Celsius, Fahrenheit, and Kelvin.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

print("=== Temperature Converter ===")
print("1. Convert from Celsius")
print("2. Convert from Fahrenheit")
print("3. Convert from Kelvin")

choice = int(input("Enter your choice (1/2/3): "))
temperature = float(input("Enter the temperature value: "))

if choice == 1:
    print(f"{temperature}°C = {celsius_to_fahrenheit(temperature):.2f}°F")
    print(f"{temperature}°C = {celsius_to_kelvin(temperature):.2f}K")

elif choice == 2:
    print(f"{temperature}°F = {fahrenheit_to_celsius(temperature):.2f}°C")
    print(f"{temperature}°F = {fahrenheit_to_kelvin(temperature):.2f}K")

elif choice == 3:
    print(f"{temperature}K = {kelvin_to_celsius(temperature):.2f}°C")
    print(f"{temperature}K = {kelvin_to_fahrenheit(temperature):.2f}°F")

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
