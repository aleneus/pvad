# Python 3 как инструмент анализа данных

## Введение

Здравствуйте!

* Необходимость рассказать о каких-то инструментах. Скоро практики.
* Python - популярное решение. Но не единственное.
* Очень много материалов, нет проблем
* Использование в исследованиях
* Прототипирование, проблемы переписывания кода

Пулл-реквест в эту лекцию приветствуется.

## Установка Python 3

### windows

![](./pic/python-site.png)

Варианты загрузки:

![](./pic/downloads.png)

Вариант для установки:

![](./pic/usual.png)

Встраиваемый Python

![](./pic/embed.png)

Содержимое архива:

![](./pic/archive.png)

Допустим, вы распаковали архив в папку `D:lec\`.

Создайте там файл `hello.py` со следующим содержимым:

```
print('Hello, world!')
```

Чтобы запустить программу, выполните команду:

```
python.exe hello.py
```

### Ubuntu

```
$ sudo apt update
$ sudo apt install python3
```

### Онлайн-сервисы

  ![](./pic/online.png)

## Установка пакетов

Удобно использовать pip. Принцип работы. PyPI. Ссылка.

### windows

Просто pip, без 3 на конце.

```
> pip install package_name
```

`sudo` означает выполнение действия от имени суперпользователя.

Обновление уже установленного пакета:

```
> pip install -U package_name
```

Установка в папку пользователя

```
> pip install --user package_name
```

### Ubuntu

Следует использовать команду `pip3`, если речь идет о Python 3 (скорее
всего, это так).

```
$ sudo pip3 install package_name
```

Здесь `sudo` означает выполнение действия от имени суперпользователя.

### Виртуальное окружение, virtualenv

TODO

## Jupyter notebook

* Установка
* Запуск
* Настройка

  ```
  $ cd jupyter
  $ jupyter notebook
  ```

  В браузере должна открыться вкладка:

  ![](./pic/jupyter.png)

  Пример страницы:

  ![](./pic/jupyter-example.png)

* Совместная работа

* Я его не люблю, но иногда использую

## Пакеты

### Визуализация

#### matplotlib

Ссылка. Основные возможности. Принцип работы. Выполнение действий от
имени `pyplot`.

#### plotly

TODO

Примеры есть в лекции об аномалиях в данных.

### Организация данных

#### numpy

Массив. Низкоуровневая реализация.

#### pandas

Data Frame.

В прошлом году я читал лекцию по организации данных для машинного
обучения. Я положил сюда примеры, которые я тогда
показывал. Посмотрите. <!-- TODO: ссылка -->

### Статистика

scipy.stats. TODO: текст

### Машинное обучение

sklearn.

наборы данных, datasets

## Другие инструменты, API для Python

Перенесение кода на низкий уровень, реализация на другом языке
программирования. Python как клей. Ограничения подхода.

Наш опыт переписывания библиотеки обработки сигналов.

tensorflow

## Ссылки

* [Python](https://www.python.org/)
* [Online Python](https://repl.it/languages/python3)
* [Python. Урок 16. Установка пакетов в
  Python](https://devpractice.ru/python-lesson-16-install-packages/)
* [Виртуальная среда Python –
  Основы](https://python-scripts.com/virtualenv)
* [Обработка данных](https://pythonworld.ru/obrabotka-dannyx)
* [Анализ данных с использованием
  Python](https://habr.com/ru/post/353050/)
* [Plotly Python Open Source Graphing
  Library](https://plotly.com/python/)
* [Statistical functions
  (scipy.stats)](https://docs.scipy.org/doc/scipy/reference/stats.html)
* [scikit-learn. Machine Learning in
  Python](https://scikit-learn.org/stable/index.html)
* [PyBrain работаем с нейронными сетями на
  Python](https://habr.com/ru/post/148407/)
* [Основы анализа данных на python с использованием
  pandas+sklearn](https://habr.com/ru/post/202090/)
* [An end-to-end open source machine learning
  platform](https://www.tensorflow.org/)
* [Введение в машинное обучение с
  tensorflow](https://habr.com/ru/post/326650/)
* [Сравнение программ глубинного
  обучения](https://ru.wikipedia.org/wiki/%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC_%D0%B3%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)
* [Машинное обучение для начинающих: создание нейронных
  сетей](https://python-scripts.com/intro-to-neural-networks)
