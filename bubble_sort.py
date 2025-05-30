def bubble_sort(arr):
    if len(arr) <= 1: return arr
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]: arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

tester = [2, 3, 4, 1, 5, 93, 56, 4]
print(tester)
print(bubble_sort(tester))

"""
sour@OR3 super-journey % python3 bubble_sort.py
[2, 3, 4, 1, 5, 93, 56, 4]
[1, 2, 3, 4, 4, 5, 56, 93]
"""
