"""Компьютер загадывает целое число от 1 до 100. 
    И компьютер должен отгадать загаданное число менее чем за 20 попыток"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """ Алгоритм угадывания рандомного число менее чем за 20 попыток
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    number = np.random.randint(1, 101)
    min = 0
    max = 100

    while True:
        predict = round((min+max)/2)
        count += 1
        if number == predict:
            break
        elif number > predict:
            min = predict
        elif number < predict:
            max = predict
    
    return count


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    return score


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)