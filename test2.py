def add(x, y):
# Тази функция събира две числа
   return x + y

def subtract(x, y):
# Тази функция изважда две числа
   return x - y

def multiply(x, y):
# Тази функция умножава две числа
   return x * y

def divide(x, y):
# Тази функция дели две числа
   return x / y


# Вход на потребителя
print("ИЗБЕРИ ОПЕРАЦИЯ.")
print()
print("1.СЪБИРАНЕ")
print("2.ИЗВАЖДАНЕ")
print("3.УМНОЖЕНИЕ")
print("4.ДЕЛЕНИЕ")
print()

choice = input("Въведи число от 1 до 4: ")

print()
if choice in ['1', '2', '3', '4']:
 num1 = int(input("Въведе първото число: "))
 
if choice in ['1', '2', '3', '4']:
 num2 = int(input("Въведи второто число: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("ВЪВЕДИ ЧИСЛО ОТ 1 ДО 4 !!! ")