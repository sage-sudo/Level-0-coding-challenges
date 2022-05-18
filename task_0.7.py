def celsius_to_fahrenheit(temp):
    temperature_in_celsius = float(temp)
    convert_to_fahrenheit = (temperature_in_celsius * (9/5)) + 32

    return f"{convert_to_fahrenheit :.3f} Degrees in Fahrenheit"


def fahrenheit_to_celsius(temp):
    temperature_in_fahrenheit = float(temp)
    convert_to_celsius = (temperature_in_fahrenheit - 32) / (9/5)
    return f"{convert_to_celsius :.2f} Degrees in Celsius"


fahrenheit = celsius_to_fahrenheit(42)
print(fahrenheit)
celsius = fahrenheit_to_celsius(107.600)
print(celsius)


