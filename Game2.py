import random


def run():
    DIGITS = '0123456789'
    new_game = True

    print("Игра «Быки и коровы»")
    print("Я загадал число из 4 разных цифр (первая цифра может быть 0).")
    print("Бык значит, что цифра угадана и стоит на своём месте.")
    print("Корова значит, что цифра есть в числе, но стоит на другом месте.")

    while new_game:
        # Загадываем 4 разные цифры
        secret = ''.join(random.sample(DIGITS, 4))
        attempts = 0
        print("\nЯ загадал число. Попробуйте угадать!")

        while 1:
            guess = input("Ваш вариант: ").strip()

            # Проверка правильности ввода
            if len(guess) != 4 or not all(ch in DIGITS for ch in guess):
                print("Нужно ввести ровно 4 цифры. Попробуйте снова.")
                continue
            if len(set(guess)) != 4:
                print("Цифры не должны повторяться. Попробуйте снова.")
                continue

            attempts += 1

            # непосредственно подсчёт быков и коров
            bulls = 0
            cows = 0
            for i in range(4):
                if guess[i] == secret[i]:
                    bulls += 1
                elif guess[i] in secret:
                    cows += 1

            print(f"Быки: {bulls}, коровы: {cows}")

            if bulls == 4:
                print(f"\nПоздравляю! Вы угадали число {secret}!")
                print(f"Количество попыток: {attempts}")
                break

        # Предложение новой игры
        while 1:
            answer = input("\nСыграем ещё раз? (да/нет): ").strip().lower()
            if answer in ('да'):
                new_game = True
                print()
                break
            elif answer in ('нет'):
                new_game = False
                print()
                break
            else:
                print("Введите «да» или «нет».")