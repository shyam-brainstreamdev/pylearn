numbers = [5,8,2,7,1]
numbers.sort()
print(numbers)
new_list = sorted(numbers)
print(new_list)
numbers.sort(reverse=True)
print(numbers)

students = [
    {"name": "Shyam", "age": 18},
    {"name": "Rohit", "age": 18},
    {"name": "Bhavik", "age": 42},
    {"name": "Vaibhav", "age": 38}
]
students.sort(key=lambda x: x["age"])
print(students)

words = ["apple", "kiwi", "banana", "fig"]
words.sort(key=len)
print(words)

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
print(bubble_sort(numbers))

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr
print(selection_sort(numbers))

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    return arr
print(insertion_sort(numbers))

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort(numbers))

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(numbers, 8))

def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
numbers = [10,20,30,40,50,60,70]
print(binary_search(numbers, 50))