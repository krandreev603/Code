# конвертор на дължина от инчове в сантиметри.
def inches_to_cm(inches):
    return inches * 2.54

inches = float(input("Въведете дължина в инчове: "))

centimeters = inches_to_cm(inches)
print(f"{inches:.2f} инча = {centimeters:.2f} сантиметра")
