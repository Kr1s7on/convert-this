"""

                         #       #  #    #      
### ### ##  # # ### ### ###     ### ###      ## 
#   # # # # # # ##  #    #       #  # #  #   #  
### ### # #  #  ### #    ##      ## # #  ## ##  

by @Kr1s7on                                             
"""

import json

HISTORY_FILE = "conversion_history.json"

def load_history():
    """Load history from a JSON file."""
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_history(history):
    """Save history to a JSON file."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

def show_menu():
    """Display the main menu."""
    print("""
                         #       #  #    #      
### ### ##  # # ### ### ###     ### ###      ## 
#   # # # # # # ##  #    #       #  # #  #   #  
### ### # #  #  ### #    ##      ## # #  ## ##  

by @Kr1s7on
    """)
    print("1. Length (meters to feet, feet to meters)")
    print("2. Weight (kilograms to pounds, pounds to kilograms)")
    print("3. Currency (USD to EUR, EUR to USD)")
    print("4. View Conversion History")
    print("5. Temperature (Celsius to Fahrenheit, Fahrenheit to Celsius)")
    print("6. Volume (liters to gallons, gallons to liters)")
    print("7. Speed (km/h to mph, mph to km/h)")
    print("8. Time (seconds, minutes, hours)")
    print("q. Quit")
    print("=========================")

def convert_length(history):
    """Convert between meters and feet."""
    print("\n--- Length Converter ---")
    try:
        value = float(input("Enter value: "))
        unit = input("Enter unit (m for meters, ft for feet): ").lower().strip()
        if unit == "m":
            result = f"{value} meters = {value * 3.28084:.2f} feet"
        elif unit == "ft":
            result = f"{value} feet = {value / 3.28084:.2f} meters"
        else:
            raise ValueError("Invalid unit. Please enter 'm' or 'ft'.")
        print(result)
        history.append(result)
        save_history(history)
    except ValueError as e:
        print(f"Error: {e}")

def convert_weight(history):
    """Convert between kilograms and pounds."""
    print("\n--- Weight Converter ---")
    try:
        value = float(input("Enter value: "))
        unit = input("Enter unit (kg for kilograms, lb for pounds): ").lower().strip()
        if unit == "kg":
            result = f"{value} kg = {value * 2.20462:.2f} lb"
        elif unit == "lb":
            result = f"{value} lb = {value / 2.20462:.2f} kg"
        else:
            raise ValueError("Invalid unit. Please enter 'kg' or 'lb'.")
        print(result)
        history.append(result)
        save_history(history)
    except ValueError as e:
        print(f"Error: {e}")

def convert_currency(history):
    """Convert between USD and EUR."""
    print("\n--- Currency Converter ---")
    try:
        value = float(input("Enter value: "))
        unit = input("Enter unit (usd for US dollars, eur for Euros): ").lower().strip()
        exchange_rate = 0.92  # Example rate: 1 USD = 0.92 EUR
        if unit == "usd":
            result = f"{value} USD = {value * exchange_rate:.2f} EUR"
        elif unit == "eur":
            result = f"{value} EUR = {value / exchange_rate:.2f} USD"
        else:
            raise ValueError("Invalid unit. Please enter 'usd' or 'eur'.")
        print(result)
        history.append(result)
        save_history(history)
    except ValueError as e:
        print(f"Error: {e}")

def view_history(history):
    """Display conversion history."""
    print("\n--- Conversion History ---")
    if not history:
        print("No conversion history found.")
    else:
        for entry in history:
            print(entry)

def convert_temperature(history):
    """Convert between Celsius and Fahrenheit."""
    print("\n--- Temperature Converter ---")
    try:
        value = float(input("Enter value: "))
        unit = input("Enter unit (c for Celsius, f for Fahrenheit): ").lower().strip()
        if unit == "c":
            result = f"{value} °C = {(value * 9/5 + 32):.2f} °F"
        elif unit == "f":
            result = f"{value} °F = {((value - 32) * 5/9):.2f} °C"
        else:
            raise ValueError("Invalid unit. Please enter 'c' or 'f'.")
        print(result)
        history.append(result)
        save_history(history)
    except ValueError as e:
        print(f"Error: {e}")

def convert_volume(history):
    """Convert between liters and gallons."""
    print("\n--- Volume Converter ---")
    try:
        value = float(input("Enter value: "))
        unit = input("Enter unit (l for liters, gal for gallons): ").lower().strip()
        if unit == "l":
            result = f"{value} L = {(value * 0.264172):.2f} gal"
        elif unit == "gal":
            result = f"{value} gal = {(value / 0.264172):.2f} L"
        else:
            raise ValueError("Invalid unit. Please enter 'l' or 'gal'.")
        print(result)
        history.append(result)
        save_history(history)
    except ValueError as e:
        print(f"Error: {e}")

def convert_speed(history):
    """Convert between km/h and mph."""
    print("\n--- Speed Converter ---")
    try:
        value = float(input("Enter value: "))
        unit = input("Enter unit (kmh for km/h, mph for miles/hour): ").lower().strip()
        if unit == "kmh":
            result = f"{value} km/h = {(value / 1.60934):.2f} mph"
        elif unit == "mph":
            result = f"{value} mph = {(value * 1.60934):.2f} km/h"
        else:
            raise ValueError("Invalid unit. Please enter 'kmh' or 'mph'.")
        print(result)
        history.append(result)
        save_history(history)
    except ValueError as e:
        print(f"Error: {e}")

def convert_time(history):
    """Convert between seconds and minutes/hours."""
    print("\n--- Time Converter ---")
    try:
        value = float(input("Enter value: "))
        unit = input("Enter unit (s for seconds, m for minutes, h for hours): ").lower().strip()
        if unit == "s":
            result = f"{value} seconds = {value/60:.2f} minutes = {(value/3600):.2f} hours"
        elif unit == "m":
            result = f"{value} minutes = {value*60:.2f} seconds = {(value/60):.2f} hours"
        elif unit == "h":
            result = f"{value} hours = {value*3600:.2f} seconds = {(value*60):.2f} minutes"
        else:
            raise ValueError("Invalid unit. Please enter 's', 'm', or 'h'.")
        print(result)
        history.append(result)
        save_history(history)
    except ValueError as e:
        print(f"Error: {e}")

def main():
    """Main function to run the unit converter."""
    history = load_history()
    while True:
        show_menu()
        choice = input("Choose an option: ").lower().strip()

        if choice == "1":
            convert_length(history)
        elif choice == "2":
            convert_weight(history)
        elif choice == "3":
            convert_currency(history)
        elif choice == "4":
            view_history(history)
        elif choice == "5":
            convert_temperature(history)
        elif choice == "6":
            convert_volume(history)
        elif choice == "7":
            convert_speed(history)
        elif choice == "8":
            convert_time(history)
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, 8, or Q.")

if __name__ == "__main__":
    main()
