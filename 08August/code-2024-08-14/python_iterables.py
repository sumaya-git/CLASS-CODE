

# unpaking dictionary

person ={
    'name': 'Thomas',
    'age': 30

}

# def introduce(name,age):
#     return f'Hello, my name is {name}. I am {age} years old.'         #function

# print(introduce('Alexander',28))
# print(introduce('Elizabeth', 23))

# print(introduce(**person))



person_1 ={
    'name': 'Thomas',
    'age': 30,
    'position': 'Developer'

}


person_2 ={
    'name': 'Emily',
    'age': 28,
    'position': 'Marketer'

}


# all_person = {**person_1, **person_2}                #if key same it will over write

# print(all_person)




# Iterables
# List, Tuple, Set, Dictionary

# len()
activities = ['Walking', 'Running', 'Talking', 'Eating']

# print(len(activities))                # len will provide how many elements are there


# enumerate() is listing number

# print('Todo list')

# for i, j in enumerate(activities, 1):
#     print(f'{i}. {j}')  


weather = {
    'temperature': 22,
    'condition': 'Sunny',
    'location': 'Paris'
}

# for i in weather:
#     print(i)

# for count, data in enumerate(weather, 1):   
#     print(f'{count}.{data}: {weather[data]}')

# for count, data in enumerate(weather.items(), 1):   
#     print(f'{count}. {data[0]}: {data[1]}')



# Zip()


# all_products = ['Laptop', 'Phone', 'Monitor']

# all_prices = [1200, 800, 400]


# for product, price in zip(all_products, all_prices):
    # print(f'{product} cost {price} euro.')



# max, min, sum

all_prices = [1200, 800, 400, 20]

# def find_max(data):
#     return max(data)

# print(find_max(all_prices))

# print(max(all_prices))
# print(min(all_prices))
# print(sum(all_prices))

# def find_max(data):
#     val = max(data)
#     return f'The maximum value is {val}'

# print(find_max(all_prices))


# shopping_cart = {
#     'product_1': 1000,
#     'product_2': 500,
#     'product_3': 50,

# }


# print(sum(shopping_cart.values()))


# sorted()

all_prices = [1200, 800, 400, 20]


sorted_prices = sorted(all_prices)

# print(sorted_prices)

# all_prices = [1200, 800, 400, 20]
# def sorting_func(item):
#     if item > 100:
#         return item
#     else: 
#         return -1

# sorted_prices = sorted(all_prices, key=sorting_func)

# print(sorted_prices)


#########
shopping_cart = {
    'product_2': 1000,
    'product_1': 500,
    'product_3': 50,

}

# def sorting_func(item):
#     return shopping_cart[item]
   

# sorted_prices = sorted(shopping_cart, key=sorting_func)

# print(sorted_prices)

# exercise from yesterday

# books = {
#   'Harry Potter And The Sorcerer\'s Stone': 1241100000,
#   'Harry Potter And The Chamber Of Secrets': 771300000,
#   'Harry Potter And The Prisoner Of Azkaban': 65210000,
#   'Harry Potter And The Goblet Of Fire': 645600000,
#   'Harry Potter And The Order Of The Phoenix': 635600000,
#   'Harry Potter And The Half Blood Prince': 661300000,
#   'Harry Potter And The Deathly Hallows ': 652200000,
# }

# def book_func(x):
#     return x[1]


# new_books = sorted(books.items(), reverse=True, key=book_func)

# print(new_books)



# lamda function

def square(x):
    return x**2

def double(x):
    return x*2



# print(square(5))
# print(double(50))


# multiply_by_2 = lambda x: x * 2

# print(multiply_by_2(20))



# def addition(a, b, c):
#     return a + b+ c


# book_lambda = lambda x: x[4:]

# day = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

# print(book_lambda(day))


# numbers = [2, 5, 10] # [4, 10, 20]
# e = []

# for i in numbers:
#     d = i * 2
#     e.append(d)

# print(e)

#map()

# numbers = [2, 5, 10] # [4, 10, 20]

# double_func = lambda x: x * 2

# new_numbers = list(map(double_func, numbers))

# print(new_numbers)


#filter

numbers = [2, 5, 10, 15, 20, 30] # [5, 15]

num_lambda = lambda x: x % 2 == 1

odd_numbers = list(filter(num_lambda, numbers))

print(odd_numbers)
# print(list(filter(lambda x: x % 2 == 0, numbers)))     #short form


















