"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 100)

count = 0

while True:
    count+=1
    predict_number = int(input("Угадай числа от 1 до 100  "))
    
    if predict_number > number:
        print("Число меньше")
    elif predict_number < number:
        print("Число больше")
    else:
        print(f"Вы угадали! Число = {number}, за {count} попыток")
        break    