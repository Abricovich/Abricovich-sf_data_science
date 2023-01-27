# [Проект 0. Угадай число](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_0/game.ipynb)

## Оглавление

[1. Описание проекта](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_0/README.md#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем?](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_0/README.md#2-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Краткая информация о данных](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_0/README.md#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

[4. Этапы работы над проектом](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_0/README.md#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[5. Результаты](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_0/README.md#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)

[6. Выводы](https://github.com/Abricovich/Abricovich-sf_data_science/blob/master/project_0/README.md#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

### 1. Описание проекта
Угадать загаданное компьютером число за минимальное число попыток

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 2. Какой кейс решаем?
Необходимо написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования**
- Компьютер загадывает целое число от 0 до 100 и нам его нужно угадать. Под "угадать" подразумевается "написать программу, которая угадывает число".
- Алгоритм учитывает больше или меньше случайное число, необходимого нам.

**Метрика качества**

Результаты оцениваются по среднему количеству попыток при 1000 повторениях. Алгоритм считается успешным при условии, что среднее число попыток угадывания не превышает 20

**Что практикуем**

- Учимся писать хороший код на Python
- Учимся работать с IDE.
- Учимся работать с GitHub.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 3. Краткая информация о данных
.........

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 4. Этапы работы над проектом
- Создаём функцию score_game, генерирующую рандомно последовательность из 1000 чисел в диапазоне от 1 до 100
- Задаём алгоритм угадывания загаданного числа и прописываем его в функцию random_predict:

-*вначале сравнивается среднее число диапазона чисел от 1 до 100(число 50) с загаданным числом*

-*если загаданное число больше, то диапазон чисел сужается(при первой попытке, например, от 50 до 100), и берётся среднее число нового диапазона(число округляется до целого) если загаданное число меньше, то диапазон чисел сужается(при первой попытке, например, от 1 до 50), и берётся среднее число нового диапазона(число округляется до целого)*

-*цикл продолжается до того момента пока не будет найдено загаданное число, после этого цикл останавливается и количество попыток угадывания по каждому числу передаётся функцией random_predict обратно в score_game*

- Score_game считает среднее число попыток угадывания алгоритма для выборки из 1000 чисел, и выводит на экран

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 5. Результаты
Созданный алгоритм рабочий и показал результаты угадывания в 4 раза лучше, чем ставилось в условии задания(20 попыток).

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### 6. Выводы
Созданный алгоритм интегрирован в программу game_v2, и показал угадывание числа в среднем за 5 попыток на выборке из 1000 случайных чисел.

:arrow_up:[к оглавлению](https://github.com/Abricovich/Abricovich-sf_data_science/tree/master/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)








