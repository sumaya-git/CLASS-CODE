

# Creating lambda function


def addition(a, b):
    return a+b
# print(addition(20, 30))

add_lambda = lambda a, b: a + b

# print(add_lambda(70, 30))


def maxim(x,y): 
     if x > y: 
        return x
     else:
         return y


maximum = lambda x, y: x if x > y else y


# print(maxim(2, 200))

# print(maximum(3, 300))





# Find the square of a number------>

square_num = lambda n: n**2

# print(square_num(20))


# Concatenate two string together ---------->

'Hello', 'Daniel'

concatenate_lambda = lambda x, y: x +' '+ y   # or
concate = lambda str1, str2: f'{str1} {str2}'
# print(concatenate_lambda('Hello', 'Daniel'))


# find ever num in lambda-------------->


is_even = lambda x: x % 2 == 0

# print(is_even(4))


is_odd = lambda x: x % 2 != 0

# print(is_odd(4))


# reverse string---------------->

reverse_str = lambda a: a[::-1]

# print(reverse_str('shayaan'))
# print(reverse_str('shariq'))


# lambda with map

number = [1, 2, 3, 4, 5]


multi_num = lambda x: x*10

# print(list(map(multi_num, number)))



# using for loop-------->

numbers = [1, 2, 3, 4, 5] # --> [10, 20, 30, 40, 50]

empty_list = []

for num in numbers:
    empty_list.append(num * 10)

# print(empty_list)

# making set------------>
new_set = set(map(lambda n: n*10, range(5))) 

# print(new_set)




num = range(10, 20)

# print(list(map(lambda x:x * 100, num)))




sen_1 = 'Race'
sen_2 = 'Life is a maze'


long_text = lambda text_1, text_2: text_1 if len(text_1) > len(text_2) else text_2
# print(long_text('Race', 'Life is a maze.'))


word =  ['maria', 'python', 'atlantic']

capitalized_list = list(map(lambda word: word.capitalize(), word))


# print(capitalized_list)


word =  ['maria', 'python', 'atlantic']

capitalized_list = list(map(lambda word: word.upper(), word))


# print(capitalized_list)


# List comprehention---------->


numbers = [1, 2, 3, 4, 5]

new_number = [x*10 for x in numbers]

# print(new_number)




# product = ['Laptop', 'Monitor', 'Keyboard', 'cap', 'Headphone', 'home', 'tech', 'Lunch']

# print([p for p in['Product' ]if len(p)>5])


# Create a list of dictionary from two given lists using list comprehension.

list_1 = ['name', 'age', 'is_employee']
list_2 = ['Ahmed', 37, 'True']

{'name': 'Ahmed', 'age': 37, 'is_employee': True}







list_1 = ['name', 'age', 'is_employee']
list_2 = ['Ahmed', 37, 'True']

{'name': 'Ahmed', 'age': 37, 'is_employee': True}

new_list = [{x:y} for x,y in zip(list_1, list_2)]

print(new_list)
                                                







# given_list = ['Laptop', 'Monitor', 'Keyboard', 'cap', 'Headphone', 'home', 'tech', 'Lunch']

# resulting_list = [x.upper() for x in given_list if len(x) < 5 and x[0] == 'M']

# print(resulting_list)
















