import argparse
import re
from math import sqrt

parser = argparse.ArgumentParser(description="Задание 2")
parser.add_argument("circle_file", type=str, help="Путь к файлу с координатами окружности и радиуса")
parser.add_argument("dot_file", type=str, help="Путь к файлу с координатами точек")
args = parser.parse_args()
circle_file = args.circle_file
dot_file = args.dot_file

max_dots = 100  # Максимальное кол-во точек

circle_data_dict = {}  # Словарь для хранения координат и радиуса окружности
with open(circle_file, "r", encoding='utf-8') as f:
    content = []
    for line in f:
        content.append(re.split(r"[ \n]", line))
    content[0].pop()
    circle_data_dict['coordinates'] = dict.fromkeys(['x', 'y'])
    circle_data_dict['coordinates']['x'] = int(content[0][0])
    circle_data_dict['coordinates']['y'] = int(content[0][0])
    circle_data_dict['radius'] = int(content[1][0])

dot_data_dict = {}  # Словарь для хранения координат произвольных точек
with open(dot_file, "r", encoding='utf-8') as f:
    content = []
    for count, line in enumerate(f, start=1):
        if count >= max_dots:  # Проверка на кол-во точек
            print('Количество точек должно быть меньше 100!')
            break
        content_lst = re.split(r"[ \n]", line)
        if '' in content_lst:
            content_lst.remove('')
        content.append(content_lst)
    for i in range(len(content)):
        dot_data_dict[f'dot {i + 1}'] = dict.fromkeys(['x', 'y'])
        dot_data_dict[f'dot {i + 1}']['x'] = int(content[i][0])
        dot_data_dict[f'dot {i + 1}']['y'] = int(content[i][1])

if count < max_dots:
    x_circle = circle_data_dict['coordinates']['x']
    y_circle = circle_data_dict['coordinates']['x']
    r_circle = circle_data_dict['radius']

    for dot in dot_data_dict.values():  # Для каждой точки рассчитываем дистанцию и печатаем ответ
        distance = sqrt((dot['x'] - x_circle) ** 2 + (dot['y'] - y_circle) ** 2)
        if distance < r_circle:
            print(1)
        elif distance == r_circle:
            print(0)
        else:
            print(2)
