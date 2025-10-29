# калкулатор за ДДС:Напишете програма, която по въведена цена на стока и ставка на ДДС изчислява сумата на ДДС и общата цена.

price = float(input("Въведете цена на стоката: "))
vat_rate = float(input("Въведете процент на ДДС (%): "))

vat_amount = price * vat_rate / 100
total_price = price + vat_amount

print(f"Сума на ДДС: {vat_amount:.2f} лв.")
print(f"Обща цена с ДДС: {total_price:.2f} лв.")
