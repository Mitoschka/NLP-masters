# Task 1

## Описание файлов
- **female_names_rus.txt**: текстовый файл с женскими именами;
- **male_names_rus.txt**: текстовый файл с мужскими именами;
- **names.txt**: объединенный текстовый файл со всеми именами;
- **names_test.txt**: тестовая выборка имён;
- **names_train.txt**: тренировочная выборка имён;
- **requirements.txt**: модули и пакеты, используемые в проекте;
- **data.py**: скрипт для создания `names.txt`, `names_test.txt`, `names_train.txt`;
- **train.py**: скрипт для обучения модели;
- **test.py**: скрипт для теста модели;
- **model.pth**: веса обученной модели;
- **stoi.pth**: словарь обученной модели.

## Запуск скриптов
Для запуска `data.py` необходимо скачать файлы `female_names_rus.txt` и `male_names_rus.txt` *[из репозитория]([https://www.markdownguide.org](https://github.com/Raven-SL/ru-pnames-list/tree/master/lists)https://github.com/Raven-SL/ru-pnames-list/tree/master/lists)*. Затем в консоли прописать:
```
python data.py
```

Для запуска `train.py` в консоль необходимо прописать:
```
python train.py names_train.txt
```

Для запуска `test.py` в консоль необходимо прописать:
```
python test.py model.pth names_test.txt
```
