def plus_minus(arr: list):
    list_of_numbers_negatives = []
    list_of_numbers_positives = []
    list_of_numbers_zeros = []
    for number in arr:
        if number < 0:
            list_of_numbers_negatives.append(number)
        elif number == 0:
            list_of_numbers_zeros.append(number)
        else:
            list_of_numbers_positives.append(number)
            
    return f'{(len(list_of_numbers_positives)/len(arr)):.6f} \n{(len(list_of_numbers_negatives)/len(arr)):.6f} \n{(len(list_of_numbers_zeros)/len(arr)):.6f}'


print(plus_minus([-4, 3, -9, 0 ,4, 1]))
