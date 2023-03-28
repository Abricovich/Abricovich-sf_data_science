import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    sqft = float(input('Введите sqft: '))
    zipcode = int(input('Введите zipcode: '))
    longitude = float(input('Введите долготу: '))
    latitude = float(input('Введите широту: '))
    baths = float(input('Введите количество ванных комнат: '))
    age = int(input('Введите возраст дома: '))
    rating_mean = float(input('Введите срединий рейтинг школ: '))
    lotsize = float(input('Введите площадь участка: '))
    stories = int(input('Введите этаж дома: '))
    distance_mean = float(input('Средняя дистанция до школ: '))
    beds = int(input('Введите количество комнат: '))

    r = requests.post('http://localhost:5000/predict', json=[sqft, zipcode, longitude, latitude, baths, age, rating_mean, lotsize, stories, distance_mean, beds])
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)