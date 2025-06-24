# Big O нотация — это способ описания сложности алгоритмов. Она показывает,
# как время выполнения или использование памяти увеличивается при росте размера входных данных n.

# O(1) - константа
# O(n^2) - квадратичная



# O(n) - линейная
def find_element(arr, elem):
    for i in arr:
        if i == elem:
            return print(f"{i}")
    return print("нету")

my_list = [1,23,4,54,5,5,67,658,679,80,80,89,00,789]

find_element(my_list,5)

# O (long n)
def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        print(f"Left:{left} ----- Right:{right}")
        mid = (left + right) // 2
        print(f"Numb--{lst[mid]}==== Index--{mid}")
        if lst[mid] == target:
            return print(f"index--{mid} Numb---{lst[mid]}")
        elif lst[mid] < target:
            left = mid +1
        else:
            right = mid - 1
    return "Нету"

my_array = [1, 3, 18, 5, 7, 9, 11, 13, 14, 15, 16, 17 ,20]

binary_search(my_array, 18)


