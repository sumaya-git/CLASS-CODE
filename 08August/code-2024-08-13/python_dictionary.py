

# Dictionary

'''
*key,value pairs
'''
# Creating Dictionary

person = {}
person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age':28, 'email': 'alex@gmail.com'}

shopping_cart = dict(laptop = 1299, smartphone = 799, keyboard = 30 )

# print(person)

# print(type(person)) 

# print(shopping_cart)
# print(type(shopping_cart))

person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age':28, 'email': 'alex@gmail.com'}


# print(person['email'])
# print(person['age'])
# print(person)

# person['last_name'] = 'Thompson'                #change value

# print(person)

# person['phone_no'] = 12345678
# person['phone_no'] = '+4912345678'                 #add key
# print(person)

#combaind
names = ['Alex', 'Emily', 'Thomas']
ages = [22, 19, 23]

person = dict(zip(names, ages))

# print(person)


#Dictionary methods

person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age':28, 'email': 'alex@gmail.com', 'address': 'South port 34'}
# print(person)
# person.clear()
# print(person)


# user = person.copy()

# print(user)


# print(person.get('email'))
# print(person.get('address', 'North street 27'))

person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age':28, 'email': 'alex@gmail.com'}


# print(person.pop('last_name'))         #remove element
# print(person.popitem())

# print(person)




# names = ['Alex', 'Emily', 'Thomas']
# ages = [22, 19, 23]

# user = dict(zip(names, ages))

person = {'first_name': 'Alex', 'last_name': 'Simpson', 'age':28, 'email': 'alex@gmail.com'}
user = {'Alex': 22, 'Emily': 19, 'Thomas': 23}

# print(user.update({'James': 24}))
# print(user)


# person.update(user)

# print(person)

user = {'Alex': 22, 'Emily': 19, 'Thomas': 23, 'email': 'alex.bob@gmail.com'}
# print(user.setdefault('contact'))
# print(user)

food_list = ['Pizza', 'Burger', 'Doner', 'Bread', 'Butter']

food_dict = dict.fromkeys(food_list, 'Discount 30%')
food_dict['Burger'] = 'Discount 50%'

# print(food_dict)



# Nested dictionary


person = {
            'first_name': 'Alex',
            'last_name': 'Simpson',
            'age': 28,
            'email': 'alex@gmail.com',
            'address': {
                'house_no': 44,
                'street_name': 'South port',
                'phone:no': '+49123456789'
            }
          }


# print(person['address'])



# for i in person:
#     if i['name']['first_name'] == 'Thomas':             #finding position
#         print(i['email'][2])
#         print(person.index(i))













