# Проект 3. LightAutoML

## Оглавление
[1. Описание проекта](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем?](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#2-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Краткая информация о данных](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

[4. Этапы работы над проектом](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[5. Результаты](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)

[6. Выводы](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

### 1. Описание проекта
Представьте, что вы работаете стажером в компании, которая продает подержанные автомобили, и в какой-то момент к вам приходит руководитель с предложением построить модель для предсказания адекватной стоимости машины по ее характеристикам из объявления.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 2. Какой кейс решаем?
Построить модель для предсказания адекватной стоимости машины по ее характеристикам из объявления на примере AutoML.

**Условия соревнования**
- Данное соревнование является бессрочным и доступно для всех потоков.
- Тестовая выборка представлена в Лидерборде целиком. Поэтому лучшие и победные решения буду проверяться на их "адекватность" (чтоб не было подгонки под тестовую выборку).
- Разрешено использовать любые ML алгоритмы и библиотеки (кроме DL).
- Делаем реальный ML продукт, который потом сможет нормально работать на новых данных

**Метрика качества**
- Решение оформлено согласно требованиям "Условия соревнования"
- Соблюдены и выполнены все этапы проекта с заданиями, представлены выводы и графики
- Метрикой в данном соревновании является MAE - среднее абсолютное отклонение (mean absolute error)
- Ваш сабмит в соревнование должен выглядеть как sample_submission.csv файл - содержать 10697 строк с предсказаниями для каждого row_ID от 35000 до 45696 включительно.
- Решение размещено на Git hub, submit на [Kaggle](https://www.kaggle.com/competitions/sf-dst-predict-car-price/overview)

**Что практикуем**

Учимся писать хороший код на Python, практикуем: написание функций, умения выбирать и применять статистические тесты, проверять гипотезы,
базовые/продвинутые методы работы  с данными в Pandas, визуализацию, построение модели машинного обучения на примере AutoML

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 3. Краткая информация о данных
- Исходный тренировочный датасет(train_data) размещён на [ресурсе](https://drive.google.com/uc?id=1XWWqJeuVmHubRbj5LwDj8937q3m7D3IZ)
- Тестовый датасет(test_data) размещён на [ресурсе](https://drive.google.com/uc?id=1HMVOlV73TJzxjhibsKiZPecY_r4Il2O1)
- Сабмит(sample_submission) размещён на [ресурсе](https://drive.google.com/uc?id=1gZi--O7G82NWgVO3wvZTINXqZA4dmD8t)


:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 4. Этапы работы над проектом
- Базовый анализ структуры данных, преобразование данных
- Преобразование данных, EDA
- Моделирование
- Резюме

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
 
### 5. Результаты
Построена модель по предсказанию цены автомобиля по его характеристикам, сделаны предсказания по сабмиту, результат направлен в соревнование на платформе [Kaggle](https://www.kaggle.com/competitions/sf-dst-predict-car-price/overview) для определения метрики

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 6. Выводы
Преобразованы данные, созданы новые признаки, построена модель AutoML и выполнены предсказания цены автомобиля по характеристикам, получены реузультаты метрики на платформе Kaggle.
 
:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)








