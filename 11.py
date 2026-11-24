import requests

def random_soviet():
    url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["slip"]["advice"]
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе API: {e}"

print("Случайный совет")
print(random_soviet())

