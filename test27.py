#(14)Напише те програма, която чете от конзолата списък с числа и след това изчислява и отпечатва средната стойност на числата.
numbers = input("Въведете числа, разделени с интервал: ").split()
num_list = []
for num in numbers:
    num_list.append(int(num))
average = sum(num_list) / len(num_list) if num_list else 0
print("Средната стойност на числата е:", average)
