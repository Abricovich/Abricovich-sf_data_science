# Проект 8. Анализ временных рядов на примере ВВП Ганы

## Оглавление
[1. Описание проекта](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем?](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#2-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Краткая информация о данных](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

[4. Этапы работы над проектом](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[5. Результаты](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)

[6. Выводы](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

### 1. Описание проекта
В данном проекте необходимо проанализировать ВВП африканской страны Гана. Предстоит исследовать временной ряд, изучить его свойства, построить модели и сделать выводы по результатам.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 2. Какой кейс решаем?


**Цели проекта**
1. Произвести предобработку набора данных.
2. Выполнить анализ и оценку и исследование временного ряда.
3. Выбрать и построить модели.
4. Выполнить и оценить предсказание ВВП на 2023 год.
5. Сделать выводы по проекту.

**Метрика качества**
- Выполнены цели проекта
- Соблюдены и выполнены все этапы проекта с заданиями, представлены обоснования и графики
- Сделаны выводы на всех этапах проекта
- Решение размещено на Git hub

**Что практикуем**

- Работа со статистическими моделями: MA, ARMA, ARIMA, SARIMAX
- Интерполяция и сэмплирование временных рядов
- Валидация временных рядов
- Модели прогнозирования гетероскедастичности
- PROPHET
- Модели классического ML 

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 3. Краткая информация о данных
- Датасет содержит ВВП африканской страны Гана. Предоставлены показатели ВВП Ганы за 62 года. - расположены на [ресурсе](https://lms.skillfactory.ru/assets/courseware/v1/cf3fb9ca311981f5cc6b6f0a40621388/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/ghana_gdp.zip).

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 4. Этапы работы над проектом
1. **Базовый анализ и знакомство с данными**
2. **Оценка ряда, выбор модели**
3. **Построение модели, подбор параметров**
4. **Интерполяция. Построение моделей на интерполированных данных**
5. **Предсказание волатильности. Прогнозирование гетероскедастичности**
6. **PROPHET**
7. **Итоги**

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
 

### 5. Результаты
Произведен анализ временного ряда на примере ВВП Ганы, подобрана оптимальная модель, выполнены предсказания ВВП на 2023 год.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 6. Выводы
Задачи проекта выполнены полностью с соблюдением всех этапов. Полные выводы по каждому этапу сформированы в Project_8_ML. 
 
:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_6#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)








