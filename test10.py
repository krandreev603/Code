# калкулатор за деление с извеждане на остатък.

dividend = int(input("Въведете делимото (цяло число): "))
divisor = int(input("Въведете делителя (цяло число): "))

if divisor == 0:
    print("Грешка: Деление на нула не е позволено.")
else:
    quotient = dividend // divisor     
    remainder = dividend % divisor   

    print(f"{dividend} ÷ {divisor} = {quotient} с остатък {remainder}")
