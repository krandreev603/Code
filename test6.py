# Задача за конвертор на валути
rates = {
    "BGN": 1.0,       # Български лев
    "EUR": 1.95583,   # Евро към лев
    "USD": 1.68       # Долар към лев
}

amount = float(input("Въведете сума: "))
from_currency = input("От валута (BGN, EUR, USD): ").upper()
to_currency = input("Към валута (BGN, EUR, USD): ").upper()

if from_currency in rates and to_currency in rates:
    amount_in_bgn = amount * rates[from_currency]
    converted = amount_in_bgn / rates[to_currency]
    print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("Невалидна валута. Моля, използвайте BGN, EUR или USD.")
