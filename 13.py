import requests

def random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["text"]
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе API: {e}"

print("Случайный факт")
print(random_fact())

