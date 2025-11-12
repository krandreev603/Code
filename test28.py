#(15)Напишете програма, която чете от конзолата списък с числа и след това премахва всички отрицателни числа от списъка.
numbers = int(input("Въведете брой числа в списъка: "))
num_list = []
for _ in range(numbers):
    num = int(input("Въведете число: "))
    num_list.append(num)
num_list = [num for num in num_list if num >= 0]
print("Списък без отрицателни числа:", num_list)