# Предположим, что данные о кругах загружены из файла в таком же формате:

from math import pi, sqrt

from task3.Circle import Circle


# Проверка, содержится ли один круг внутри другого
def contains(circle1, circle2):
    dist = distance(circle1["center"], circle2["center"])
    # Круг circle1 содержит circle2, если расстояние между их центрами плюс радиус второго круга меньше радиуса первого
    return dist + circle2["radius"] <= circle1["radius"]


# Функция для расчета расстояния между двумя точками
def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def read_circles_from_file(file_path):
    circles = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            if len(parts) == 3:
                x, y, radius = map(float, parts)
                circles.append(Circle(x, y, radius))
    return circles


circles = read_circles_from_file("test_input_1")

# Создаем объекты класса Circle на основе этих данных
#circles = [Circle(x, y, r) for x, y, r in circles_data]

# Подсчет количества кругов внутри каждого круга и определение круга с максимальным количеством
contains_count = [0] * len(circles)

for i, outer in enumerate(circles):
    for j, inner in enumerate(circles):
        if i != j and contains({"center": outer.center, "radius": outer.radius},
                               {"center": inner.center, "radius": inner.radius}):
            contains_count[i] += 1

# Идентификация круга с максимальным количеством вложенных кругов
max_contains = max(contains_count)
candidates = [i for i, count in enumerate(contains_count) if count == max_contains]

# Выбор круга с максимальной площадью среди кандидатов
max_area = 0
best_circle_index = None
for i in candidates:
    area = pi * circles[i].radius ** 2
    if area > max_area:
        max_area = area
        best_circle_index = i

print(best_circle_index, circles[best_circle_index].center, circles[best_circle_index].radius, max_area)
