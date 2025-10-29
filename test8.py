# калкулатор за площ на правоъгълен триъгълник.
def triangle_area(base, height):
    return (base * height) / 2

base = float(input("Въведете дължината на основата (катет): "))
height = float(input("Въведете височината (другия катет): "))

area = triangle_area(base, height)

print(f"Площта на правоъгълния триъгълник е: {area:.2f} квадратни единици")
