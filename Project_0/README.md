# Игра: Угадай число

## Оглавление  
1. [Описание проекта](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
2. [Какой кейс решаем?](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)
3. [Краткая информация о данных](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)
4. [Этапы работы над проектом](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)
5. [Результат](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)
6. [Выводы](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)
7. [Ссылка](https://colab.research.google.com/drive/10PKYkNs6sUQzON2rSx608roi0QuRg-7v?usp=sharing) на файл в облачном хранилище google

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Краткая информация о данных
**Условия соревнования:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Этапы работы над проектом  
В ходе реализации проекта были выбран метод бинарного поиска. Были установлены 3 переменные left, right и center для индексов. Была уставлена последовательность number_range от 1 до 100. Для подсчета попыток был установлен счетчик count, который записывает количество итераций. В цикле while начинали искать число от середины последовательности. Если загаданное число было больше/ меньше середины, то отбрасывали половину последовательности. Далее сдвигали индексы left, right  по последовательности и center, с которм сравнивали искомое число. Когда center равнялся искомому числу, цикл заканчивает свою работу. [код](https://github.com/Irinaeva/data_science/blob/main/Project_0/game.py).


:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Результаты:  
По [результатам опробирования](https://github.com/Irinaeva/data_science/blob/main/Project_0/game.ipynb) алгоритм справляется за 4 попытки.

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Выводы:
Метод бинарного поиска работает меньше чем за 20 попыток в последовательности от 1 до 100

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

