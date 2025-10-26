def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Риби"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнаци"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лъв"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Везни"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козирог"
    else:
        return "Невалидна дата"

while True:
    try:
        day = int(input("Въведи ден на раждане (1-31): "))
        month = int(input("Въведи месец на раждане (1-12): "))
        zodiac = get_zodiac_sign(day, month)
        print()
        print(f"Твоята зодия е: {zodiac}")
    except ValueError:
        print("Моля, въведи валидни числа за ден и месец.")

    repeat = input("Искаш ли да въведеш нова дата? (да/не): ").strip().lower()
    if repeat != "да":
        print("Благодаря! До скоро!")
        break
