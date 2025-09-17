# Lab 2 - Recursive Functions

# Part B - Programming

# 1. Factorial (recursive)
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

# 2. Linear Search (recursive)
def linear_search(lst, key, index=0):
    if index >= len(lst):
        return -1
    if lst[index] == key:
        return index
    return linear_search(lst, key, index + 1)

# 3. Binary Search (recursive)
def binary_search(lst, key, left=0, right=None):
    if right is None:
        right = len(lst) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if lst[mid] == key:
        return mid
    elif lst[mid] < key:
        return binary_search(lst, key, mid + 1, right)
    else:
        return binary_search(lst, key, left, mid - 1)
