# Реализовать функцию:
# в которой все отрицательные элементы массива списка перенести в его начало,
# а все остальные – в конец,
# сохраняя исходное взаимное расположение как среди отрицательных,
# так и среди остальных элементов.
# Дополнительный список или массив не заводить.

import random


def create_random_list(amount_of_elems):
    list = []
    for i in range(amount_of_elems):
        list[i].append(random.randint(-10, 10))
    return list


def get_list_from_file(path):
    file = open(path, 'r')
    line = file.read()
    list = line.split(" ")
    for i in range(len(list)):
        list[i] = int(list[i])
    file.close()
    return list

def write_list_to_file(path, list):
    file = open(path, 'w')
    for elem in list:
        file.write(str(elem) + " ")
    file.close()


def solution(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] >= 0 and list[j + 1] < 0:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


list = get_list_from_file('task1_input.txt')

list = solution(list)

write_list_to_file('task1_output.txt', list)


