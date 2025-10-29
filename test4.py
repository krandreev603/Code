num1 = float(input("Въведете първото число: "))
num2 = float(input("Въведете второто число: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
quot_result = num1 / num2 if num2 != 0 else None

print(f"Сума: {sum_result:.2f}")
print(f"Разлика: {diff_result:.2f}")
print(f"Произведение: {prod_result:.2f}")
if quot_result is not None:
    print(f"Частно: {quot_result:.2f}")
else:
    print("Частно: Деление на нула!")