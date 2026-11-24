import random
import textwrap

MIN_COUNT = 1
MAX_COUNT = 1000
LIMIT = 10 ** 10  # допустимые границы


def ask_int(prompt, low, high):
    """Запрашивает целое число в диапазоне [low, high], пока ввод не станет корректным."""
    while True:
        text = input(prompt).strip()
        try:
            if "_" in text:
                raise ValueError 
            value = int(text)
        except ValueError:
            print("Please enter an integer.")
            continue
        if not low <= value <= high:
            print(f"The number must be between {low} and {high}.")
            continue
        return value


def ask_range():
    """Запрашивает границы диапазона. Нижняя граница не должна быть больше верхней."""
    while True:
        low = ask_int(f"Enter the lower bound ({-LIMIT} to {LIMIT}): ", -LIMIT, LIMIT)
        high = ask_int(f"Enter the upper bound ({-LIMIT} to {LIMIT}): ", -LIMIT, LIMIT)
        if low <= high:
            return low, high
        print("The lower bound must not be greater than the upper bound. Try again.\n")


def generate_numbers(count, low, high):
    """Возвращает список из count случайных целых чисел из диапазона [low, high]."""
    return [random.randint(low, high) for _ in range(count)]


def ask_play_again():
    while True:
        answer = input("Generate again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")


def run():
    print("=== Random number generator ===")
    while True:
        count = ask_int(f"How many numbers ({MIN_COUNT} to {MAX_COUNT})? ", MIN_COUNT, MAX_COUNT)
        low, high = ask_range()

        numbers = generate_numbers(count, low, high)

        print(f"\nGenerated {count} number(s) in range [{low}, {high}]:\n")
        print(textwrap.fill(", ".join(map(str, numbers)), width=80))
        print()

        if not ask_play_again():
            print()
            break


if __name__ == "__main__":
    run()
