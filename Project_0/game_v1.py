
import numpy as np
def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

number = np.random.randint(1, 101) # загадываем число
count = 0

while True:
    count += 1
    pretdict_number = int(input('Угодай число от 1 до 100'))
    
    if pretdict_number > number:
        print('Число должно быть меньше!')
        
    elif pretdict_number < number:
        print('Число должно быть больше!')
        
    else:
        print(f'Вы угодали число! Это число {number} за {count} попыток')
        break   