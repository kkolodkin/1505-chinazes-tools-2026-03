import secrets
import string

def get_valid_length():
    """Запрашивает у пользователя длину пароля и проверяет её корректность."""
    while True:
        try:
            length = int(input("Введите длину пароля (от 1 до 100): "))
            if 1 <= length <= 100:
                return length
            else:
                print("Ошибка: длина должна быть в диапазоне от 1 до 100.")
        except ValueError:
            print("Ошибка: введите целое число.")

def get_yes_no(question):
    """Универсальная функция для получения ответа Да/Нет."""
    while True:
        answer = input(f"{question} (да/нет): ").strip().lower()
        if answer in ['да', 'д', 'yes', 'y']:
            return True
        elif answer in ['нет', 'н', 'no', 'n']:
            return False
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'.")

def generate_password(length, use_digits, use_special, use_uppercase):
    """Генерирует пароль на основе заданных параметров."""
    # Базовый набор символов (всегда доступен)
    char_pool = string.ascii_lowercase
    
    # Опциональные наборы
    if use_digits:
        char_pool += string.digits
    if use_special:
        # Экранируем спецсимволы, которые имеют значение в регулярных выражениях или строках
        char_pool += "!@#$%^&*()_+{}:\"<>?,./;'[]\\|`~"
    if use_uppercase:
        char_pool += string.ascii_uppercase

    if not char_pool:
        # Эта проверка нужна на случай, если пользователь отключит все опции (хотя в данном ТЗ lowercase включен всегда)
        raise ValueError("Набор символов пуст. Включите хотя бы один тип символов.")

    # Генерация пароля с использованием криптографически стойкого выбора
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    return password

def main():
    print("=== Генератор паролей ===")
    
    length = get_valid_length()
    use_digits = get_yes_no("Использовать цифры")
    use_special = get_yes_no("Использовать спецсимволы")
    use_uppercase = get_yes_no("Использовать заглавные буквы")

    try:
        password = generate_password(length, use_digits, use_special, use_uppercase)
        print(f"\nВаш сгенерированный пароль:\n{password}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()