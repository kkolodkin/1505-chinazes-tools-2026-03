import random

import requests

API_URL = "https://the-trivia-api.com/v2/questions"
REQUEST_TIMEOUT = 10  # секунды


def fetch_question():
    """Получает один случайный вопрос с API.

    Возвращает словарь:
        {"text": str, "options": [str, ...], "correct": str}
    Бросает requests.RequestException при проблемах с сетью и
    ValueError при неожиданном формате ответа.
    """
    response = requests.get(API_URL, params={"limit": 1}, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list):
        if not data:
            raise ValueError("API returned an empty list")
        data = data[0]

    try:
        question = data["question"]
        # в API v2 вопрос лежит в question.text, на случай строки - тоже поддерживаем
        text = question["text"] if isinstance(question, dict) else question
        correct = data["correctAnswer"]
        incorrect = list(data["incorrectAnswers"])
    except (KeyError, TypeError) as error:
        raise ValueError(f"Unexpected API response format: {error}")

    options = incorrect + [correct]
    random.shuffle(options)
    return {"text": text, "options": options, "correct": correct}


def ask_question(question):
    """Показывает вопрос и варианты. Возвращает:
        True  - ответ верный,
        False - ответ неверный,
        None  - пользователь решил закончить игру.
    """
    print(f"\n{question['text']}\n")
    for number, option in enumerate(question["options"], start=1):
        print(f"{number}. {option}")
    print("q. Finish the game")

    while True:
        answer = input("\nYour answer: ").strip().lower()
        if answer == "q":
            return None
        if answer.isdigit() and 1 <= int(answer) <= len(question["options"]):
            chosen = question["options"][int(answer) - 1]
            if chosen == question["correct"]:
                print("Correct!")
                return True
            print(f"Wrong! The correct answer is: {question['correct']}")
            return False
        print(f"Please enter a number from 1 to {len(question['options'])} or 'q'.")


def ask_retry():
    """После ошибки загрузки спрашивает, пробовать ли снова."""
    while True:
        answer = input("Try again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")


def run():
    print("=== Quiz ===")
    print("Answer the questions. Enter 'q' instead of an answer to finish.")

    score = 0
    answered = 0

    while True:
        try:
            question = fetch_question()
        except requests.RequestException as error:
            print(f"\nCould not load a question (network problem): {error}")
            if ask_retry():
                continue
            break
        except ValueError as error:
            print(f"\nCould not read the question: {error}")
            if ask_retry():
                continue
            break

        result = ask_question(question)
        if result is None:
            break

        answered += 1
        if result:
            score += 1
        print(f"Score: {score} / {answered}")

    print(f"\nGame over! Your score: {score} out of {answered}.\n")


if __name__ == "__main__":
    run()
