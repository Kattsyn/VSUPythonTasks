def get_file_matrix(file_name):
    matrix = []
    file = open(file_name, 'r')
    for line in file:
        row = line.split()
        for i in range(len(row)):
            row[i] = int(row[i])
        matrix.append(row)
    return matrix


def write_matrix_to_file(file_name, matrix):
    file = open(file_name, 'w')
    for row in matrix:
        for col in row:
            file.write(str(col) + " ")
        file.write("\n")
    file.close()


def set_flags_for_matrix(matrix):
    for row in matrix:
        row.append(check_row_for_sequence(row))


def delete_flags_from_matrix(matrix):
    for row in matrix:
        row.pop()


def check_row_for_sequence(row):
    flag = True
    for i in range(1, len(row)):
        if row[i] < row[i - 1]:
            flag = False
            return flag
    return flag


def sort_matrix(matrix):
    set_flags_for_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix) - 1):
            if not matrix[j][-1] and matrix[j + 1][-1]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
    delete_flags_from_matrix(matrix)



matrix = get_file_matrix("task2_test_1")
sort_matrix(matrix)
write_matrix_to_file("new_file", matrix)

