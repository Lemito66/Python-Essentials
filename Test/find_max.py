
    #max_num = float('-inf')
    
def find_max(nums):
    max_num = float('-inf')
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([1, 4, 2, 8, 5, 7]))