import pandas as pd

def get_city_inf():
    """ Парсит сайт http://amerikos.com/geo/?pageNumber=1&pageLimit=120 
    с данными по городам/штатам/округам/zip-code

    Returns:
        DateFrame: спарсенные данные с сайта упакованные в датафрейм
    """   
    # начинаем парсить с первой страницы
    page = 1
    # адрес сайта, в котором будет меняться переменная pageNumber
    url = f'http://amerikos.com/geo/?pageNumber={page}&pageLimit=120'
    # вывод информации о номере страницы
    print(f'Парсим {page} страницу')
    # считываем инфо со страницы - тип данных - лист, в котором необходим элемент 2
    df = pd.read_html(url)[2]
    # временный датафрейм
    df_temp = df    
    # запускаем цикл останавливающийся по условию
    while df_temp['Город'].iloc[0] != 'Не удалось найти города.':
        # увеличиваем счётчик страниц
        page += 1
        # выводим информацию на какой странице находимся
        print(f'Парсим {page} страницу')
        # обновляем адрес страницы
        url = f'http://amerikos.com/geo/?pageNumber={page}&pageLimit=120' 
        # данные записываем во временный датафрейм      
        df_temp = pd.read_html(url)[2]
        # производим объединение датафреймов(основоного и временного) построчно
        df = pd.concat(
            [df, df_temp],
            ignore_index=True,
            axis=0
        )
    # удаляем последнюю неинформативную строку    
    df = df.drop(axis=0, index=(df.shape[0]-1))
    return df