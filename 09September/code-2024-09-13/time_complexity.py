
# Time complex

# def greet(day):
#     print('Hello all, Have a great start of the day.')


# greet('Friday')


# def division(*args):
#     return args[0] / 10

# print(division(30, 50, 100))


# def pick_last(lst):
#     return lst[-1]


# print(pick_last([30, 7, 100, 5, 80, 20]))



import time
start = time.time()

# print(pick_last([30, 7, 100, 5, 80, 20, 555]))

end = time.time()

# print(f'Execution time: {end - start}')


# O(n)


def get_items(lst):
    n = len(lst)
    for i in range(n):
        print(lst[i])


get_items([30, 7, 100, 5, 80, 20, 555])




def get_items(lst):
    n = len(lst)            # --> O(1)
    for i in range(n):
        print(lst[i])       # --> O(n)


start = time.time()

get_items([30, 7, 100, 5, 80, 20, 555]) # --> O(1) + O(n) ~ O(n)

end = time.time()

# print(f'Execution time: {end - start}')




# O(n^2)

# def make_pair(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(n):
#             print(lst[i], lst[j])


# numbers = [30, 7, 100, 5, 80, 20, 555]

# make_pair(numbers)



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(7))




num_list = [55, 80, 3, 12, 70, 20, 133, 7, 200, 45]

            # [55, 80,]

# --> [3, 7, 12, 20, 45, 55, 70, 80, 133, 200]

  # print(lst[i])       # --> O(n)


# start = time.time()

# get_items([30, 7, 100, 5, 80, 20, 555]) # --> O(1) + O(n) ~ O(n)

# end = time.time()

def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

print(f'Original list: {num_list}')
print(f'Sorted list: {bubble_sort(num_list)}')

