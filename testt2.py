from testt import get_zodiac_sign

while True:
    try:
        day = int(input("Въведи ден на раждане (1-31): "))
        month = int(input("Въведи месец на раждане (1-12): "))
        zodiac =get_zodiac_sign(day, month)
        print()
        print(f"Твоята зодия е: {zodiac}")
    except ValueError:
        print("Моля, въведи валидни числа за ден и месец.")
        
    repeat = input("Искаш ли да въведеш нова дата? (да/не): ").strip().lower()
    if repeat != "да":
        print("Благодаря! До скоро!")
        break
