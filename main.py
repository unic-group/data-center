import requests

# Замените <YOUR_TOKEN> на ваш собственный токен API
token = "<YOUR_TOKEN>"

# URL API Click для создания платежной сессии
create_session_url = "https://api.click.uz/pay"

# URL API Click для завершения платежа
complete_payment_url = "https://api.click.uz/pay/complete"

# Заголовок запроса с токеном API
headers = {
    "Authorization": f"Bearer {token}"
}

def create_payment_session(amount, phone, merchant_trans_id):
    # Данные для создания платежной сессии
    data = {
        "amount": amount,  # Сумма платежа в тиынах
        "phone": phone,  # Номер телефона пользователя
        "merchant_trans_id": merchant_trans_id  # Уникальный идентификатор платежа
    }

    # Отправка POST-запроса к Click API для создания платежной сессии
    response = requests.post(create_session_url, json=data, headers=headers)

    # Проверка статуса ответа
    if response.status_code == 200:
        payment_session = response.json()
        return payment_session
    else:
        return None

def complete_payment(payment_id, merchant_trans_id):
    # Данные для завершения платежа
    data = {
        "payment_id": payment_id,  # Идентификатор платежной сессии
        "merchant_trans_id": merchant_trans_id  # Уникальный идентификатор платежа
    }

    # Отправка POST-запроса к Click API для завершения платежа
    response = requests.post(complete_payment_url, json=data, headers=headers)

    # Проверка статуса ответа
    if response.status_code == 200:
        payment_result = response.json()
        return payment_result
    else:
        return None

# Пример использования
amount = 1000
phone = "998XXXXXXXXX"
merchant_trans_id = "123456789"

# Создание платежной сессии
payment_session = create_payment_session(amount, phone, merchant_trans_id)
if payment_session:
    print("Платежная сессия создана:", payment_session)
    payment_id = payment_session["payment_id"]

    # Ваш код для отображения платежной формы пользователю

    # Подтверждение платежа
    payment_result = complete_payment(payment_id, merchant_trans_id)
    if payment_result:
        print("Платеж завершен:", payment_result)
        # Ваш код для обработки успешного платежа
    else:
        print("Произошла ошибка при завершении платежа")
        # Ваш код для обработки неудачного платежа
else:
    print("Произошла ошибка при создании платежной сессии")
    # Ваш код для обработки ошибки создания платежной сессии