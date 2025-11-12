#(16)Напишете програма, която чете от конзолата списък с числа и след това го сортира по низходящ ред.
numbers = int(input("Въведете брой числа в списъка: "))
num_list = []
for _ in range(numbers):
    num = int(input("Въведете число: "))
    num_list.append(num)
num_list.sort(reverse=True)
print("Сортиран списък по низходящ ред:", num_list)