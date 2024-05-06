# Resume analysis. Model for determining wages.

## Оглавление  
1. [Описание проекта](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
2. [Какой кейс решаем?](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)
3. [Краткая информация о данных](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)
4. [Этапы работы над проектом](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)
5. [Результат](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)
6. [Выводы](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)
7. [Ссылка](https://colab.research.google.com/drive/10PKYkNs6sUQzON2rSx608roi0QuRg-7v?usp=sharing) на файл в облачном хранилище google

### Описание проекта    
Построить модель для опредления заработной платы через анализ резюме соискателей.

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
### Какой кейс решаем?    
Построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю, исходя из информации, которую он указал о себе в резюме.

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Краткая информация о данных
**Условия:**  
- Прежде чем построить модель, данные необходимо преобразовать, исследовать и очистить. .
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Верное предсказание модели

**Что практикуем**     
 * Базовый анализ струткры данных
 * Преобразование данных
 * Разведывательный анализ
 * Очистка данных

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Этапы работы над проектом  
Знакомство с данными и исследование их структуры, какие типы данных хранятся.
Предобработка данных, т.к. признаки представлены в неудобном для анализа и очистки формате.
Визуально оценить зависимости в данных: построить гистограмму распределения зарплаты и возраста, столбчатую диаграмму  зарплаты по уровню образования и другое. Провести разведовательный анализ для выявления связей между признаками, выявления закономерностей, определения распределений признаков, поиска аномалий и других дефектов данных.
Заполнить пропущенные значения числовыми константами или найти выбросы. Мы нашли несколько несостыковок в данных: пропуски, гигантские размеры желаемых заработных плат, резюме людей слишком «преклонного» возраста, опыт работы, превышающий возраст. Эти данные подлежат очистке.
[код](https://github.com/Irinaeva/data_science/blob/main/Project_0/game.py).


:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Результаты:  
По [результатам опробирования](https://github.com/Irinaeva/data_science/blob/main/Project_0/game.ipynb) модель прогнозирует желаемый уровень заработной платы.

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Выводы:
Проведен основыне этапы работы с данными для постороения модели.

:arrow_up:[к оглавлению](https://github.com/Irinaeva/data_science/blob/main/Project_0/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

