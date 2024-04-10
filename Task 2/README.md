# Task 2
## Описание файлов
- **GPTLanguageModel**: директория с результатами работы дефолтной модели;
	- **exponent_losses.txt**: текстовый файл с экспоненциальными оценками потерь; 
	- **losses.png**: график с экспоненциальными оценками потерь;
	- **model.pth**: полученная модель после обучения;
	- **more.txt**: результат сгенерированного контекста;
- **GPTLanguageModelWithSwitch**: директория с результатами работы Switch Transformer;
	- **exponent_losses.txt**: текстовый файл с экспоненциальными оценками потерь; 
	- **losses.png**: график с экспоненциальными оценками потерь;
	- **model.pth**: полученная модель после обучения;
	- **more.txt**: результат сгенерированного контекста;
- **gpt.py**: исполнительный файл с кодом (скрипт);
- **perplexity.png**: barchart c оценками perplexity моделей;
- **ru.txt**: текстовый файл [Мастер и Маргарита](https://github.com/averkij/woland)

## Предварительные надстройки
Внутри исполняемого файла `gpt.py` необходимо указать:
- **PATH**: путь к расположению файлов;
- **model**: одна модель из двух ( `GPTLanguageModel` | `GPTLanguageModelWithSwitch` )

## Пример вывода консоли
### GPTLanguageModel
```
step 0: train loss 4.5424, val loss 4.5399
step 500: train loss 2.1746, val loss 2.1559
step 1000: train loss 1.5182, val loss 1.6074
step 1500: train loss 1.3014, val loss 1.4853
step 2000: train loss 1.1665, val loss 1.4586
step 2500: train loss 1.0521, val loss 1.4503
step 3000: train loss 0.9470, val loss 1.4786
step 3500: train loss 0.8465, val loss 1.5124
step 4000: train loss 0.7465, val loss 1.5607
step 4500: train loss 0.6596, val loss 1.6177
step 4999: train loss 0.5752, val loss 1.6876
```
### GPTLanguageModelWithSwitch
```
step 0: train loss 4.5424, val loss 4.5399
step 500: train loss 2.1749, val loss 2.1568
step 1000: train loss 1.5048, val loss 1.5990
step 1500: train loss 1.2878, val loss 1.4861
step 2000: train loss 1.1451, val loss 1.4627
step 2500: train loss 1.0209, val loss 1.4612
step 3000: train loss 0.9122, val loss 1.4921
step 3500: train loss 0.8097, val loss 1.5266
step 4000: train loss 0.7110, val loss 1.5906
step 4500: train loss 0.6236, val loss 1.6564
step 4999: train loss 0.5480, val loss 1.7226
```