"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)


def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celsius_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = convert_fahrenheit_to_celsius()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def convert_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit
