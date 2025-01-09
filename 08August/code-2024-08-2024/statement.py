
# Iterable, Iterator,Iteration,iter()

animals = ['Panda', 'Fox', 'Kangaroo', 'Lion', 'Cat', 'Dog']  #Iterable

animals_iterator = iter(animals)


# print(animals)
# print(animals_iterator)

# for item in animals_iterator:
#     print(item)



animals = ['Panda', 'Fox', 'Kangaroo', 'Lion', 'Cat', 'Dog']

animals_iterator = iter(animals)           #Iterator

# print(next(animals_iterator)) #Iteration
# print(next(animals_iterator))
# print(next(animals_iterator))
# print(next(animals_iterator))



# print(len(next(animals_iterator)))



# For loop

# numbers_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for item  in numbers_list:
#     print(item)
#output
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]


# numbers_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for outer_item  in numbers_list:
#     for inner_item in outer_item:
#         print(inner_item)

#output
1
2
3
4
5
6
7
8
9

numbers_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for outer_item  in numbers_list:
#     for inner_item in outer_item:
#         if inner_item == 5:
#             continue
#         print(inner_item)




daily_tasks = {
    'day_1': 'Task 1',
    'day_2': 'Task 2',
    'day_3': 'Task 3',

}

# for key in daily_tasks:
#     print(key)
#output
# day_1
# day_2
# day_3

# for value in daily_tasks.values():
#     print(value)
#output
# Task 1
# Task 2
# Task 3



# for item in daily_tasks.items():
#       print(item[0])

#output
# day_1
# day_2
# day_3

daily_tasks = {
    'day_1': 'Task 1',
    'day_2': 'Task 2',
    'day_3': 'Task 3',

}


# for key, value in daily_tasks.items():
#       print(key + '----->' +value)


#output
# day_1----->Task 1
# day_2----->Task 2
# day_3----->Task 3




daily_tasks = {
    'day_1': {
        'Tasks': {
            'task 1': 'walk',
            'task 2': 'talk'
        }
    },
    'day_2': {
        'Tasks': {
            'task 1': 'Sing',
            'task 2': 'Dance'
        }
    },

}


# for item in daily_tasks:
#     print(item)

#output
# day_1
# day_2

for item in daily_tasks:
    print(item)


















