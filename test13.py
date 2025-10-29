# изчисление на дни, часове и минути: Напишете програма, която по въведени минути изчислява колко дни, часове и останали минути съответстват на този брой.

total_minutes = int(input("Въведете брой минути: "))

days = total_minutes // (24 * 60)
remaining_minutes = total_minutes % (24 * 60)
hours = remaining_minutes // 60
minutes = remaining_minutes % 60

print(f"{total_minutes} минути = {days} дни, {hours} часа и {minutes} минути")