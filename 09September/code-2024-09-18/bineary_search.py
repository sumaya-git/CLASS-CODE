
# Binary Search

# num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # target = 30


# def binary_search(lst, target):
    
#     low = 0 # low = 0 --> 5
#     high = len(lst) - 1 # high = 9
#     while low <= high:
#         mid = (low + high) // 2  # 4.5 ~ 4

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target: # 50 < 80
#             low = mid + 1 # 4 + 1 = 5
#         else:
#             high = mid - 1 # 4 -1 = 3
    
#     return -1


# print(binary_search(num_list, 30))







# Binary Search

num_list = [10, 20, 30, 40, 50, 60, 60, 70, 70, 80, 90, 100]


def binary_search(lst, target):
    
    low = 0 
    high = len(lst) - 1 
    result = -1


    while low <= high:
        mid = (low + high) // 2  

        if lst[mid] == target:
           result = mid
           high = mid -1
        elif lst[mid] < target: 
            low = mid + 1 
        else:
            high = mid - 1 
    
    return result


print(binary_search(num_list, 70))
































