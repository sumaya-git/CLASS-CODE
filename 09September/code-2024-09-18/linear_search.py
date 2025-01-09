
# Linear Search

# num_list = [30, 7, 100, 88, 14, 3, 55, 21] # target = 88


# def linear_search(lst, target):

#     for i in range(len(lst)):
#         if lst[i] == target:
#             return i
    
#     return -1


# print(linear_search(num_list, 88))





num_list = [30, 7, 100, 88, 14, 3, 55, 21] 


def linear_min_max_search(lst):
  

    min = lst[0]
    max = lst[0]

    for num in lst[1:]:
        if num < min:
            min = num

        if num > max:
            max = num

    return min, max

    
min_value, max_value = linear_min_max_search(num_list)

print(f'Minimum: {min_value}, Maximum: {max_value}')





