# Практическая работа. Выравнивание спорадических данных

## Задание

Имеется множество S источников данных об измерениях некоторой величины x, меняющейся во времени. В каждый момент времени формируется набор значений от случайного подмножества S. Если от некоторого источника нет значения, то в течение определенного времени (настройка) считается актуальным предыдущее значение. Если это время прошло, а значение до сих пор не получено, то считается, что величина теперь имеет нуль-значение (None, nan, нет значения).

Нужно написать исходный код, который: 1) моделирует описанный процесс спорадических измерений, 2) выполняет выравнивание данных по метке времени, т.е. формирует кадры данных, в которых значения величины сопоставлены источникам данных.

Например, пусть имеются 2 источника, и данные формировались следующим образом:

```
(t=0, s=0, x=1)
(t=0, s=1, x=2)
(t=1, s=0, x=5)
(t=2, s=0, x=6)
(t=3, s=0, x=7)
(t=3, s=1, x=8)
...
```

Результат:

```
Время  Значение для s=0   Значение для s=1
t=0    1                  2
t=1    5                  2 (все еще)
t=2    6                  - (забыто)
t=2    7                  8 (обновлено)
...
```
