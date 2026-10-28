def show_status(health, attempts, coins, inventory):
    print("\n=== ТВОИ ХАРАКТЕРИСТИКИ ===")
    print("Здоровье:", health)
    print("Попытки:", attempts)
    print("Коины:", coins)
    print("Инвентарь:", inventory)


def start():
    print("\nТы оказался в заброшенном доме.")
    print("1. Пойти налево")
    print("2. Пойти направо")
    print("3. Отдохнуть")
    print("4. Выйти из игры")

    choice = input("Твой выбор: ").lower().strip()
    return choice


def left_room(health, coins, inventory):
    print("\nТы зашел в комнату.")
    print("1. Открыть шкаф")
    print("2. Осмотреть стол")
    print("3. Вернуться назад")

    choice = input("Твой выбор: ")

    if choice == "1":
        if inventory == "Ключ найден":
            print("Шкаф пустой.")
        else:
            print("Ты нашел ключ!")
            inventory = "Ключ найден"

    elif choice == "2":
        coins += 10
        print("Ты нашел 10 коинов!")

    elif choice == "3":
        print("Ты вернулся в коридор.")

    else:
        print("Неверный выбор.")
        health -= 10
        print("Ты потерял 10 здоровья.")

    return health, coins, inventory


def right_room(health, attempts, coins, inventory):
    print("\nТы подошел к выходной двери.")
    print("1. Попробовать открыть дверь")
    print("2. Вернуться назад")

    choice = input("Твой выбор: ")

    if choice == "1":
        attempts -= 1

        if inventory == "Ключ найден":
            print("Ты открыл дверь ключом!")
            print("ПОБЕДА!")
            return health, attempts, coins, inventory, True

        else:
            health -= 20
            print("Дверь заперта! Ты потерял 20 здоровья.")
            print("Найди ключ в комнате.")

    elif choice == "2":
        print("Ты вернулся в коридор.")

    else:
        print("Неверный выбор.")

    return health, attempts, coins, inventory, False


def rest(health, coins):
    print("\nТы нашел место для отдыха.")

    if coins >= 10:
        coins -= 10
        health += 20

        if health > 100:
            health = 100

        print("Ты восстановил 20 здоровья за 10 коинов!")
    else:
        print("Недостаточно коинов. Нужно 10.")

    return health, coins


health = 100
attempts = 5
coins = 0
inventory = "Пусто"
game = True

print("=== ЗАБРОШЕННЫЙ ДОМ ===")
print("Найди ключ и выберись наружу!")

while game and health > 0 and attempts > 0:
    show_status(health, attempts, coins, inventory)

    choice = start()

    if choice == "1":
        health, coins, inventory = left_room(
            health, coins, inventory
        )

    elif choice == "2":
        health, attempts, coins, inventory, won = right_room(
            health, attempts, coins, inventory
        )

        if won:
            print("Ты успешно сбежал из дома!")
            game = False

    elif choice == "3":
        health, coins = rest(health, coins)

    elif choice == "4":
        print("Ты вышел из игры.")
        game = False

    else:
        print("Неверный выбор.")

if health <= 0:
    print("\nЗдоровье закончилось. Ты проиграл!")

elif attempts <= 0 and game:
    print("\nПопытки закончились. Ты проиграл!")

print("Игра завершена!")