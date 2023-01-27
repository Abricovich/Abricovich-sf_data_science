# [Проект 5. Подбор гиперпараметров модели на примере](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_5/Kaggle_Predicting%20a%20Biological%20Response.ipynb) [Kaggle: Predicting a Biological Response](https://www.kaggle.com/c/bioresponse)

## Оглавление
[1. Описание проекта](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем?](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#2-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Краткая информация о данных](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

[4. Этапы работы над проектом](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[5. Результаты](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)

[6. Выводы](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

### 1. Описание проекта
Построение модели с дальнейшей оптимизацией гиперпараметров

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 2. Какой кейс решаем?
Построить базовые модели(Baseline) - логистическую регрессию(LogisticRegression) и случайный лес(RandomForestClassifier). Подобрать оптимальные гиперпараметры моделей четырмя методами: **GridSeachCV**, **RandomizedSearchCV**, **Hyperopt**, **Optuna**. За основу взять [Kaggle: Predicting a Biological Response](https://www.kaggle.com/c/bioresponse).

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
- Результаты оцениваются по метрике F1
- Гиперпараметры подобраны четырьмя методами
- Решение размещено на Git hub

**Что практикуем**

Учимся писать хороший код на Python, практикуем: написание функций, умения выбирать и применять статистические тесты, проверять гипотезы,
базовые/продвинутые методы работы  с данными в Pandas, визуализацию, моделирование, подбор гиперпараметров, работа с документацией

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 3. Краткая информация о данных
- Набор данных для прогнозирование биологического ответа(_train_sem09__1_.zip) размещён на [ресурсе](https://drive.google.com/uc?id=1TlCdFMDFofyN7EIrIzXwwjcMBo4yHb1a)

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 4. Этапы работы над проектом
- Базовый анализ структуры данных, преобразование данных
- Построение базовых моделей
- Моделирование и подбор гиперпараметров
- Резюме

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
 

### 5. Результаты
Получены метрики моделей при оптимальных гиперпараметрах, подобранные различными методами, проведено сравнение методов, сделаны выводы.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 6. Выводы
Задачи проекта выполнены полностью с соблюдением всех этапов. Полные выводы по каждому этапу сформированы в Kaggle_Predicting a Biological Response. 
 
:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)








