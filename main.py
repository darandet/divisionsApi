import requests


def send_request(url, token):
    data = {"method": "list_of_divisions",
            "season_id": 1231,
            "competition_id": 1266}
    headers = {"Token": token}
    request = requests.post(url, headers=headers, json=data)
    print(request.json())


if __name__ == '__main__':
    url = "https://api-tg-1.h-cp.ru"
    # Токен удалён для безопасности
    # token = ""
    send_request(url, token)
