# Task2: Строки, элементы которых не убывают
# (т.е. образуют неубывающую последовательность чисел)
# переместить в начало (вверх),
# сохранив при этом взаимное расположением перемещаемых строк.

def get_file_matrix(file_name):
    matrix = []
    try:
        file = open(file_name, 'r')
    except:
        print("Такого файла не существует.")
        return
    for line in file:
        row = line.split()
        for i in range(len(row)):
            row[i] = int(row[i])
        matrix.append(row)
    return matrix


def write_matrix_to_file(file_name, matrix : list):
    if type(matrix) is not list:
        print("В метод write_matrix пришла не матрица")
        return
    file = open(file_name, 'w')
    for row in matrix:
        for col in row:
            file.write(str(col) + " ")
        file.write("\n")
    file.close()


def set_flags_for_matrix(matrix : list):
    for row in matrix:
        row.append(check_row_for_sequence(row))


def delete_flags_from_matrix(matrix : list):
    for row in matrix:
        row.pop()


def check_row_for_sequence(row : list):
    if type(row) is list:
        flag = True
        for i in range(1, len(row)):
            if row[i] < row[i - 1]:
                flag = False
                return flag
        return flag


def sort_matrix(matrix : list):
    if type(matrix) is not list:
        print("В метод sort_matrix пришла не матрица")
        return
    set_flags_for_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix) - 1):
            if not matrix[j][-1] and matrix[j + 1][-1]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
    delete_flags_from_matrix(matrix)


matrix = get_file_matrix("task2_test_0")
sort_matrix(matrix)
write_matrix_to_file("new_file", matrix)
