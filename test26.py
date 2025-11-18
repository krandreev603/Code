#(13) Направете програма, която симулира игра на "Камък, ножица, хартия" срещу компютъра. Потребителят въвежда свой избор, а компютъра генерира случаен избор.
import random
opinions = ["камък", "ножица", "хартия"]
comuter_choice = random.choice(opinions)
user_choice = input("Въведете вашия избор (камък, ножица, хартия): ").lower()
if user_choice not in opinions:
    print("Невалиден избор! Моля, изберете камък, ножица или хартия.")
else:
    print(f"Компютърът избра: {comuter_choice}")
    if user_choice == comuter_choice:
        print("Равенство!")
    elif (user_choice == "камък" and comuter_choice == "ножица") or \
         (user_choice == "ножица" and comuter_choice == "хартия") or \
         (user_choice == "хартия" and comuter_choice == "камък"):       
        print("Вие печелите!")
    else:
        print("Компютърът печели!")
        
