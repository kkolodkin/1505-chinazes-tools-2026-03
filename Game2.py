import random


try:
    import test
except ImportError:
    test = None
    print("Warning: 'test.py' module not found. Option 1 will be disabled.")


def generate_secret_number():
    """Генерирует случайное 4-значное число с уникальными цифрами."""
    # range(10) дает цифры от 0 до 9. random.sample гарантирует уникальность.
    digits = random.sample(range(10), 4)
    return "".join(map(str, digits))


def get_bulls_and_cows(secret, guess):
    """Подсчитывает количество быков и коров."""
    bulls = 0
    cows = 0
    
    # считаем быков
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
        # Если цифра есть в загаданном числе, но не на этом месте — это корова
        elif guess[i] in secret:
            cows += 1
            
    return bulls, cows


def print_menu():
    print(
'''
============================
Menu options

1. Run Test Module
2. Play Bulls and Cows
3. Exit
============================
''')

def play_bulls_and_cows():
    """Основная логика игрового цикла."""
    secret_number = generate_secret_number()
    # Раскомментируйте строку ниже для отладки, чтобы видеть ответ
    # print(f"[DEBUG] Secret number is: {secret_number}")
    
    attempts = 0
    
    print("\nNew game started! Guess the 4-digit number.")
    print("Enter your guess (e.g., 1234). Digits must be unique.")
    
    while True:
        guess = input("Your guess: ").strip()
        
        # Проверка валидности ввода
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter exactly 4 digits.")
            continue
        if len(set(guess)) != 4:
            print("Invalid input. All digits must be unique.")
            continue
            
        attempts += 1
        bulls, cows = get_bulls_and_cows(secret_number, guess)
        
        print(f"{bulls} Bull(s), {cows} Cow(s)")
        
        if bulls == 4:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


print("Hello! Welcome to Chinazes Tools!")

while True:
    print_menu()
    user_choice = input("Select a menu option number: ").strip()
    print()
    
    if user_choice == '1':
        if test:
            test.run()
        else:
            print("The Test Module is not available.")
    elif user_choice == '2':
        play_bulls_and_cows()
    elif user_choice == '3':
        print("Bye!")
        break
    else:
        print("Invalid choice. Try again.")