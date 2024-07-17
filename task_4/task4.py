import argparse


parser = argparse.ArgumentParser(description="Задание 4")
parser.add_argument("numbers", type=str, help="Путь к файлу с числами")
args = parser.parse_args()
numbers_file = args.numbers

with open(numbers_file, 'r', encoding='utf-8') as f:
    content = f.read().split('\n')


def quicksort(arr):
    """
    Функция быстрой сортировки чисел

    :param arr: list
    :return: list
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


def func(arr):
    """
    Функция для вычисления минимального кол-ва ходов,
    требуемых для приведения всех элементов к одному числу.
    Функция принимает отсортированный список чисел.

    :param arr: list
    :return: int
    """
    count = 0  # Счетчик ходов
    pivot = len(arr) // 2  # Индекс числа к которому будем приводить остальные числа
    num = arr[pivot]  # Число к которому будем приводить остальные числа
    arr.pop(pivot)  # Удаление числа из списка
    for el in arr:
        # Цикл в котором перебираются числа из списка
        # и считается кол-во ходов
        if el < num:
            count += num - el
        elif el > num:
            count += el - num
    return count


content = [int(item) for item in content]  # Приведение к числовому типу данных которые были получены из файла.
content = quicksort(content)  # Сортировка чисел

print(func(content))
