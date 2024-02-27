import random

def solution(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] >= 0 and list[j + 1] < 0:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
list = []
for i in range(10):
    list.append(random.randint(-10,10))

print(list)
print(solution(list))
