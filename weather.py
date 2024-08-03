def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return value, fahrenheit, kelvin
    elif unit == 'F':
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, value, kelvin
    elif unit == 'K':
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit, value
    else:
        raise ValueError("Invalid unit of measurement. Use 'C', 'F', or 'K'.")

def main():
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    
    try:
        celsius, fahrenheit, kelvin = convert_temperature(value, unit)
        print(f"\nTemperature Conversions:\nCelsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
