def flippingBits(number):
    binary_numbers = []
    bi_numbers = []
    while number != 0:
        new_number = number//2
        number_binary = number%2
        binary_numbers.append(number_binary)
        if new_number <= 1:
            binary_numbers.append(new_number)
            break
        number = new_number
    for i in range(32-len(binary_numbers)):
        bi_numbers.append(0)
    return print_list(binary_numbers+bi_numbers)

def print_list(list_of_numbers:list):
    cadena = ''
    for i in list_of_numbers:
        cadena += str(i)
    return cadena[::-1]



print(len(flippingBits(1)))



