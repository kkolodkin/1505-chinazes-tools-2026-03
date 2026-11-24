import random

CHOICES = ("rock", "scissors", "paper")

# что кого побеждает
BEATS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

# допустимые варианты
ALIASES = {
    "rock": "rock", "r": "rock", "1": "rock",
    "scissors": "scissors", "s": "scissors", "2": "scissors",
    "paper": "paper", "p": "paper", "3": "paper",
}


def get_user_choice():
    """Запрашивает выбор пользователя, пока он не введет корректный вариант."""
    while True:
        print("Make your choice:")
        print("1. Rock (r)")
        print("2. Scissors (s)")
        print("3. Paper (p)")
        answer = input("Your choice: ").strip().lower()
        if answer in ALIASES:
            return ALIASES[answer]
        print("Invalid choice. Try again.\n")


def get_winner(user, system):
    """Возвращает 'user', 'system' или None (ничья)."""
    if user == system:
        return None
    if BEATS[user] == system:
        return "user"
    return "system"


def ask_play_again():
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")


def play_round():
    user = get_user_choice()
    system = random.choice(CHOICES)

    print(f"\nYou chose: {user}")
    print(f"System chose: {system}")

    winner = get_winner(user, system)
    if winner == "user":
        print("You win!")
    elif winner == "system":
        print("System wins!")
    else:
        print("It's a draw!")
    print()


def run():
    print("=== Rock, Scissors, Paper ===")
    while True:
        play_round()
        if not ask_play_again():
            print()
            break


if __name__ == "__main__":
    run()
