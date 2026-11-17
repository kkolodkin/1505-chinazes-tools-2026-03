import random


def run():
    MIN_LIMIT = -10 ** 10
    MAX_LIMIT = 10 ** 10

    new_game = True

    while new_game:
        #Ввод диапазона цифпр
        print(f"Введите диапазон загадываемых чисел "
              f"(целые от {MIN_LIMIT} до {MAX_LIMIT}).")

        while 1:
            low_str = input("Минимальное число: ").strip()
            try:
                low = int(low_str)
            except ValueError:
                print("Нужно ввести целое число. Попробуйте снова.")
                continue
            if low < MIN_LIMIT or low > MAX_LIMIT:
                print(f"Число должно быть от {MIN_LIMIT} до {MAX_LIMIT}.")
                continue
            break

        while 1:
            high_str = input("Максимальное число: ").strip()
            try:
                high = int(high_str)
            except ValueError:
                print("Нужно ввести целое число. Попробуйте снова.")
                continue
            if high < MIN_LIMIT or high > MAX_LIMIT:
                print(f"Число должно быть от {MIN_LIMIT} до {MAX_LIMIT}.")
                continue
            if high < low:
                print(f"Максимум не может быть меньше минимума ({low}).")
                continue
            break

        #Загадывашь число
        secret = random.randint(low, high)
        attempts = 0
        print(f"\nЯ загадал число от {low} до {high}. Попробуйте угадать!")

        #Само Угадывание
        while 1:
            guess_str = input("Ваш вариант: ").strip()
            try:
                guess = int(guess_str)
            except ValueError:
                print("Нужно ввести целое число. Попробуйте снова.")
                continue
            if guess < low or guess > high:
                print(f"Число должно быть в диапазоне от {low} до {high}. "
                      f"Попытка не засчитана.")
                continue

            attempts += 1

            if guess < secret:
                print("Чимло больше")
            elif guess > secret:
                print("Число меньше")
            else:
                # 4. Победа
                print(f"\nПоздравляю! Вты угадал число {secret}!")
                print(f"Количество попыток: {attempts}")
                break

        # Предложение новой игры
        while 1:
            answer = input("\nСыграем ещё? (да/нет): ").strip().lower()
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