def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)-1):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                number_to_replace      = list_of_numbers[j]
                list_of_numbers[j]     = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = number_to_replace
    return list_of_numbers



print(bubble_sort([5,45,5]))

def max_number(list_of_numbers):
    max_number = float('-inf')
    for item in list_of_numbers:
        if item > max_number:
            max_number = item
    return max_number

print(max_number([5,10,25]))

def min_number(list_of_numbers):
    min_number = float('inf')
    for item in list_of_numbers:
        if item < min_number:
            min_number = item
    return min_number

print(min_number([5,10,25,1]))

def fibonacci(how_many_numbers):
    # 0,1,1,2,3,5
    list_of_numbers = [0,1]
    for item in range(2, how_many_numbers):
        list_of_numbers.append((list_of_numbers[item-2] + list_of_numbers[item-1]))
    return list_of_numbers

print(fibonacci(5))