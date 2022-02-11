'''Игра угадай число'''

import numpy as np

number = np. random.randint(1, 101) # загадываем число

# количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input('Угадай число от 1 до 100: '))
    
    if predict_number > number:
        print('Загаданное число меньше')
    elif predict_number < number:
        print('Загаданное число больше')
    else:
        print(f'Вы угадали загаданное число {number} за {count} попыток')
        break # конец игры, выход из цикла

    


