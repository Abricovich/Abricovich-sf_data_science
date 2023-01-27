# [Проект 4. EDA + Feature Engineering. Соревнование на Kaggle](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/EDA_Project_4_model.ipynb)

## Оглавление
[1. Описание проекта](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем?](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#2-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Краткая информация о данных](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

[4. Этапы работы над проектом](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[5. Результаты](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)

[6. Выводы](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

### 1. Описание проекта
Создание модели машинного обучения по предсказыванию рейтинга отеля по данным сайта Booking на основе имеющихся в датасете данных.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 2. Какой кейс решаем?
Вы работаете дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

**Условия соревнования**
- Решение оформляется только в Jupyter Notebook
- Каждое задание выполняется в отдельной ячейке, выделенной под задание. Не следует создавать множество ячеек для решения задачи
- Код для каждого задания оформляется в одной-двух jupyter-ячейках (не стоит создавать множество ячеек для решения задачи).
- Решение должно использовать только: переменные, основные структуры данных (списки, словари, множества), циклы, функции, библиотеки numpy, pandas, matplotlib, seaborn, plotly. 
- Код должен быть читаемым и понятным: имена переменных и функций отражают их сущность, важно избегать многострочных конструкций и условий. Код оформлен согласно руководству PEP 8.
- Графики должны содержать название, отражающее их суть, и подписи осей.
- Выводы к графикам оформляются в формате Markdown под самим графиком в отдельной ячейке. Выводы должны быть представлены в виде небольших связанных предложений на русском языке.

**Метрика качества**
- Решение оформлено согласно требованиям "Условия соревнования"
- Соблюдены и выполнены все этапы проекта с заданиями, представлены выводы и графики
- Результаты оцениваются по метрике MAPE
- Делаем реальный ML продукт, который потом сможет нормально работать на новых данных.
- Решение размещено на Git hub и [Kaggle](https://www.kaggle.com/competitions/sf-booking)


**Что практикуем**

Учимся писать хороший код на Python, практикуем: написание функций, умения выбирать и применять статистические тесты, проверять гипотезы,
базовые/продвинутые методы работы  с данными в Pandas, визуализацию, моделирование, EDA+Feature Engineering

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 3. Краткая информация о данных
- Набор данных для обучения(hotels_train.csv.zip) размещён на [ресурсе](https://drive.google.com/uc?id=1ikv9SwqRQztgRwI42RNXWNsMzpEtx16Y)
- Набор данных для оценки качества(hotels_test.csv.zip) размещён на [ресурсе](https://drive.google.com/uc?id=1sN-Tlrrvf5_V-jGx22rV1hLIou9Tq4Ri)
- Файл сабмишна в нужном формате(submission.csv.zip) размещён на [ресурсе](https://drive.google.com/uc?id=13yYjKvIYLJ618-vGYuD1nImsoSMy6BNi)


:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 4. Этапы работы над проектом
- Базовый анализ структуры данных, преобразование данных
- EDA + Feature Engineering
- Моделирование
- Резюме

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
 

### 5. Результаты
Построена модель машинного обучения по предсказанию рейтинга отеля на предварительно созданных и обработанных признаках. Сделаны предсказания, результат засабмишен на [Kaggle](https://www.kaggle.com/competitions/sf-booking)

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 6. Выводы
Задачи проекта выполнены полностью с соблюдением всех этапов. Полные выводы по каждому этапу сформированы в EDA_Project_4_model. 
 
:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_4/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)








