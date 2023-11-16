def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67



if __name__ == "__main__":
  

    temperature = float(input("Enter temperature: "))
    original_unit = input("Enter original unit (C, F, or K): ").upper()

 
    if original_unit == "C":
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif original_unit == "F":
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif original_unit == "K":
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Invalid unit. Please enter C, F, or K.")
       


    print(f"{temperature} {original_unit} is equivalent to:")
    print(f"{celsius:.2f} C")
    print(f"{fahrenheit:.2f} F")
    print(f"{kelvin:.2f} K")

