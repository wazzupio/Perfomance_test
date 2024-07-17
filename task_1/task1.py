import argparse
from itertools import cycle

parser = argparse.ArgumentParser(description="Задание 1")
parser.add_argument("n", type=int, help="Длина массива")
parser.add_argument("m", type=int, help="Длина обхода массива")
args = parser.parse_args()
n = args.n
m = args.m

lst = [i + 1 for i in range(n)]  # Список чисел от 1 до n
interval = []  # Интервал
road = []  # Путь
idx = 0  # Индекс числа в списке

for el in cycle(lst):
    if idx == 0:  # Если индекс равен 0, тогда будем добавлять число в "путь"
        road.append(el)
    if len(interval) == m:
        # Если интервал заполнен, тогда заполняем новый интервал начиная с последнего элемента предыдущего интервала
        # и текущего элемента
        last_el = interval[idx - 1]
        interval = [last_el, el]
        idx = 2
        if road[0] == last_el:  # Если первое число пути равно последнему чеслу интервала, тогда завершаем программу
            break
        else:
            road.append(last_el)
    else:
        interval.append(el)  # Добавляем числа в интервал пока не будет
        idx += 1

print(road)
