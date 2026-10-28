def check_email(email):
    if "@" in email and "." in email:
        return True
    return False

def check_password(password, password2):
    if password == password2 and len(password) >= 6:
        return True
    return False

def show_status(player):
    print("\n=== ТВОИ ХАРАКТЕРИСТИКИ ===")
    print("Здоровье:", player["health"])
    print("Попытки:", player["attempts"])
    print("Коины:", player["coins"])
    print("Инвентарь:", player["inventory"])

def register():
    print("РЕГИСТРАЦИЯ ИГРОКА")

    email = input("Введите почту: ").strip()

    while not check_email(email):
        print("Неверный email")
        email = input("Введите почту: ").strip()

    password = input("Придумайте пароль: ")
    password2 = input("Повторите пароль: ")

    while not check_password(password, password2):
        print("Пароли не совпадают, или короче 6 символов")
        password = input("Придумайте пароль: ")
        password2 = input("Повторите пароль: ")

    print("Игрок успешко зарегестрирован")

    player = {
        "email": email,
        "health":100,
        "coins": 50,
        "attempts":5,
        "inventory":[]
    }
    return player

def start():
    print("\nТы оказался в заброшенном доме.")
    print("1. Пойти налево")
    print("2. Пойти направо")
    print("3. Отдохнуть")
    print("4. Посмотреть характеристики")
    print("5. Выйти из игры")

    choice = input("Твой выбор: ").strip()
    return choice


def left_room(player):
    print("\nТы зашел в комнату.")
    print("1. Открыть шкаф")
    print("2. Осмотреть стол")
    print("3. Вернуться назад")

    choice = input("Твой выбор: ").strip()

    if choice == "1":
        if "Ключ" in player["inventory"]:
            print("Шкаф пустой.")
        else:
            print("Ты нашел ключ!")
            player["inventory"].append("Ключ")

    elif choice == "2":
        player["coins"] += 10
        print("Ты нашел 10 коинов!")

    elif choice == "3":
        print("Ты вернулся в коридор.")

    else:
        print("Неверный выбор.")
        player["health"] -= 10
        print("Ты потерял 10 здоровья.")


def right_room(player):
    print("\nТы подошел к выходной двери.")
    print("1. Попробовать открыть дверь")
    print("2. Вернуться назад")

    choice = input("Твой выбор: ").strip()

    if choice == "1":
        if player["attempts"] <= 0:
            print("Попытки закончились!")
            return False

        player["attempts"] -= 1

        if "Ключ" in player["inventory"]:
            print("Ты открыл дверь ключом!")
            print("ПОБЕДА!")
            return True

        else:
            player["health"] -= 20
            print("Дверь заперта! Ты потерял 20 здоровья.")
            print("Найди ключ в комнате.")

    elif choice == "2":
        print("Ты вернулся в коридор.")

    else:
        print("Неверный выбор.")

    return False

def rest(player):
    print("\nТы нашел место для отдыха.")

    if player["coins"] >= 10:
        player["coins"] -= 10
        player["health"] += 20

        if player["health"] > 100:
            player["health"] = 100

        print("Ты восстановил 20 здоровья за 10 коинов!")
    else:
        print("Недостаточно коинов. Нужно 10.")

def game():
    player = register()
    playing = True

    print("\n=== ЗАБРОШЕННЫЙ ДОМ ===")
    print("Найди ключ и выберись наружу!")

    while playing and player["health"] > 0 and player["attempts"] > 0:
        show_status(player)
        choice = start()

        if choice == "1":
            left_room(player)

        elif choice == "2":
            won = right_room(player)

            if won:
                print("Ты успешно сбежал из дома!")
                playing = False

        elif choice == "3":
            rest(player)

        elif choice == "4":
            show_status(player)

        elif choice == "5":
            print("Ты вышел из игры.")
            playing = False

        else:
            print("Неверный выбор.")

    if player["health"] <= 0:
        print("\nЗдоровье закончилось. Ты проиграл!")

    elif player["attempts"] <= 0 and playing:
        print("\nПопытки закончились. Ты проиграл!")

    print("\nИгра завершена!")
    show_status(player)


game()