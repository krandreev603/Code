def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def stepenuvane(x, y):
   return x ** y 

def check_negative(x, y):
    if x < 0 and y < 0:
        print(" И двете числа са отрицателни.")
    elif x < 0:
        print(" Първото число е отрицателно.")
    elif y < 0:
        print(" Второто число е отрицателно.")
    print()

# Вход на потребителя
print("ИЗБЕРИ ОПЕРАЦИЯ.")
print()
print("1.СЪБИРАНЕ")
print("2.ИЗВАЖДАНЕ")
print("3.УМНОЖЕНИЕ")
print("4.ДЕЛЕНИЕ")
print("5.СТЕПЕНУВАНЕ")
print()

choice = input("Въведи число от 1 до 5: ")

print()
if choice in ['1', '2', '3', '4', '5']:
  num1 = float(input("Въведе първото число: "))
  num2 = float(input("Въведи второто число: "))
  check_negative(num1, num2)

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
  if num2 == 0:
      print(" Грешка: Деление на нула не е позволено.")
  else:
       print(num1,"/",num2,"=", divide(num1,num2))
   
elif choice == '5':
   print(num1,"^",num2,"=", stepenuvane(num1,num2)) 
else:
   print("ВЪВЕДИ ЧИСЛО ОТ 1 ДО 5 !!! ")