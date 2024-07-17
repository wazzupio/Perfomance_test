import argparse
import json

parser = argparse.ArgumentParser(description="Задание 3")
parser.add_argument("values", type=str, help="Результаты прохождения тестов с уникальными id")
parser.add_argument("tests", type=str, help="Структура для построения отчета на основе прошедших тестов")
parser.add_argument("report", type=str, help="Сюда записывается результат")

args = parser.parse_args()

values_file = args.values
tests_file = args.tests
report_file = args.report


def add_values(tests_data, change_data, change_id):
    """
    Функция принимает: словарь который нужно отредактировать,
    словарь с ключами и данными для редактирования,
    список айдишников по которым нужно отредактировать данные.
    Функция возвращает отредактированный словарь.

    :param tests_data: dict
    :param change_data: dict
    :param change_id: lst
    :return: dict
    """
    for test_el in tests_data:  # Перебираем данные в словаре
        if test_el['id'] in change_id:  # Если id находится в списке айдишников для редактирования
            test_el['value'] = change_data[test_el['id']]  # Тогда заполняем value
            if 'values' in test_el:
                # Если есть вложенность данных values
                # Вызываем функцию рекурсивно для вложенных данных
                add_values(test_el['values'], change_data, change_id)
        elif 'values' in test_el:
            # Если id не находится в списке айдишников для редактирования но есть вложенные данные
            # Вызываем функцию рекурсивно для вложенных данных
            add_values(test_el['values'], change_data, change_id)
    return tests_data


with open(tests_file, 'r', encoding='utf-8') as f:
    tests = json.load(f)

with open(values_file, 'r', encoding='utf-8') as f:
    values = json.load(f)
    change_data_dict = {}  # Словарь для хранения значений id и value. Например "2:'passed'"
    change_id_lst = []  # Список id для которых нужно заполнить значение value
    for i in values['values']:
        change_data_dict[i['id']] = i['value']  # Заполняем словать ключами и значениями
        change_id_lst.append(i['id'])  # Заполняем список айдишниками

tests['tests'] = add_values(tests['tests'], change_data_dict, change_id_lst)

with open(report_file, 'w', encoding='utf-8') as f:
    json.dump(tests, f)
