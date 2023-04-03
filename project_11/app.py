#Импортируем необходимые библиотеки
import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import numpy as np
import pandas as pd
import lightfm as lf
import nmslib
import pickle
import scipy.sparse as sparse
import plotly.express as px

# -----------------------------------------------------------------------------------------------------
# Реализуем функции необходимые для работы приложения

@st.cache
def read_files(folder_name='data'):
    """
    Функция для чтения файлов.
    Возвращает два DataFrame с рейтингами и характеристиками книг.
    """
    ratings = pd.read_csv(folder_name + '/ratings.csv')
    books = pd.read_csv(folder_name + '/books.csv')
    return ratings, books 

def make_mappers(books):
    """
    Функция для создания отображения id в title и authors.
    Возвращает два словаря:
    * Ключами первого словаря являются идентификаторы книг, а значениями - их названия;
    * Ключами второго словаря являются идентификаторы книг, а значениями - их авторы.
    """
    name_mapper = dict(zip(books.book_id, books.title))
    author_mapper = dict(zip(books.book_id, books.authors))

    return name_mapper, author_mapper

def load_embeddings(file_name='item_embeddings.pkl'):
    """
    Функция для загрузки векторных представлений.
    Возвращает прочитанные эмбеддинги книг и индекс (граф) для поиска похожих книг.
    """
    with open(file_name, 'rb') as f:
        item_embeddings = pickle.load(f)

    # Тут мы используем nmslib, чтобы создать наш быстрый knn
    nms_idx = nmslib.init(method='hnsw', space='cosinesimil')
    nms_idx.addDataPointBatch(item_embeddings)
    nms_idx.createIndex(print_progress=True)
    return item_embeddings, nms_idx

def nearest_books_nms(book_id, index, n=10):
    """
    Функция для поиска ближайших соседей, возвращает построенный индекс.
    Возвращает n наиболее похожих книг и расстояние до них.
    """
    nn = index.knnQuery(item_embeddings[book_id], k=n)
    return nn

def get_recomendation_df(ids, distances, name_mapper, author_mapper):
    """
    Функция для составления таблицы из рекомендованных книг
    Возвращает DataFrame со столбцами:
    * book_name - имя книги
    * book_author - автор книги
    * distance - значение метрики расстояния до книги
    """
    names = []
    authors = []
    #Для каждого индекса книги находим ее название и автора
    #Результаты добавляем в списки
    for idx in ids:
        names.append(name_mapper[idx])
        authors.append(author_mapper[idx])
    #Составляем DataFrame
    recomendation_df = pd.DataFrame({'book_name': names, 'book_author': authors, 'distance': distances})
    return recomendation_df

#Загружаем данные
ratings, books = read_files(folder_name='data') 
#Создаем словари для сопоставления id книг и их названий/авторов
name_mapper, author_mapper = make_mappers(books)
#Загружаем эмбеддинги и создаем индекс для поиска
item_embeddings, nms_idx = load_embeddings()

# -----------------------------------------------------------------------------------------------------
# Реализуем интерфейс приложения

# Заголовок приложения
st.title("Recomendation System Of Books")

st.markdown("""Welcome to the web page of the book recommendation app!
This application is a prototype of a recommendation system based on a machine learning model. 

To use the application, you need:
1. Enter the approximate name of the book you like
2. Select its exact name in the pop-up list of books
3. Specify the number of books you need to recommend

After that, the application will give you a list of books most similar to the book you specified""")

# Вводим строку для поиска книг
title = st.text_input('Please enter book name')
title = title.lower()

#Выполняем поиск по книгам - ищем неполные совпадения
output = books[books['title'].apply(lambda x: x.lower().find(title)) >= 0]

#Выбор книги из списка
option = st.selectbox("Select the book you need", output['title'].values)

#Проверяем, что поле не пустое
if option:
    #Выводим выбранную книгу
    st.markdown('You selected: "{}"'.format(option))
    
    #Находим book_id для указанной книги
    val_index = output[output['title'].values == option]['book_id'].values
    
    #Указываем количество рекомендаций
    count_recomendation = st.number_input(
        label="Specify the number of recommendations you need", 
        value=10
    )    
    #Находим count_recomendation+1 наиболее похожих книг
    ids, distances = nearest_books_nms(val_index, nms_idx, count_recomendation+1)
    #Убираем из результатов книгу, по которой производился поиск
    ids, distances = ids[1:], distances[1:]
    
    #Выводим рекомендации к ней
    st.markdown('Most simmilar books are: ')
    #Составляем DataFrame из рекомендаций
    df = get_recomendation_df(ids, distances, name_mapper, author_mapper)
    #Выводим DataFrame в интерфейсе
    st.dataframe(df[['book_name', 'book_author']])
    
    # Строим столбчатую диаграмму
    fig = px.bar(
        data_frame=df, 
        x='book_name', 
        y='distance',
        hover_data=['book_author'],
        title='Cosine distance to the nearest books'
    )
    # Отображаем график в интерфейсе
    st.write(fig)