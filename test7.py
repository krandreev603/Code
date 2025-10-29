# конвертиране от Целзий във Фаренхайт
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Въведете температура в Целзий: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
