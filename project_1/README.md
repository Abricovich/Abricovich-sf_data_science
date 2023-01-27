# [Проект 1. Анализ вакансий из HeadHunter](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/Project%201.ipynb)

## Оглавление
[1. Описание проекта](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем?](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#2-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Краткая информация о данных](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

[4. Этапы работы над проектом](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[5. Результаты](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)

[6. Выводы](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

### 1. Описание проекта
Компания HeadHunter хочет построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю, исходя из информации, которую он указал о себе. Но прежде чем построить модель, данные необходимо преобразовать, исследовать и очистить. В этом и состоит задача проекта.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 2. Какой кейс решаем?
Исследовать, очистить, и преобразовать датасет для дальнейшей работы. 

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
- Решение размещено на Git hub


**Что практикуем**

Учимся писать хороший код на Python, практикуем: визуализацию, написание функций,
методы очистки данных, базовые/продвинутые методы работы  с данными в Pandas 

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 3. Краткая информация о данных
- Исходный датасет размещён на [ресурсе](https://drive.google.com/file/d/164vl81i9SHURB-xJxCrMYPDdYoSxRxOs/view?usp=sharing). 
Датасет представляет из себя базу резюме, выгруженную с сайта поиска вакансий hh.ru
- Дополнительная выгрузка - [файл](https://drive.google.com/file/d/1zIIaWf_J6M3faQ13MLuPpI6YR1NS_YYe/view?usp=sharing) о курсах валют.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 4. Этапы работы над проектом
- Базовый анализ структуры данных
- Преобразование данных
- Разведывательный анализ(EDA)
- Очистка данных

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
 

### 5. Результаты
Проведён базовый и исследовательский анализ структуры данных, получен преобразованный и очищенный датасет от выбросов, дублей, сформированы новые признаки. Добавлена визуализация.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 6. Выводы
Задачи проекта выполнены полностью с соблюдением всех этапов. Полные выводы по каждому этапу сформированы в Project 1. Датасет подготовлен для следующего этапа.
 
:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_1/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)








