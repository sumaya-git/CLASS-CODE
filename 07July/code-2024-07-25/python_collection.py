

devices = ['phone', 'laptop', 'Mpnitor', 'keyboard', 'Mouse']

books = list(['Harry Poter', 'Python for Beginners', 'The Tale of Two Cities'])




# print(devices)
# print(books)
# print(type(devices))



text = 'We watched The Last of Us yesterday.'

text_list = list(text)

# print(text)
# print(text_list)


devices = ['phone', 'laptop', 'Mpnitor', 'keyboard', 'Mouse']

single_devices = devices[0]

print(single_devices)

# print(devices.index('keyboard'))




# print(devices[0:3])

# print(devices[::-1])


devices = ['phone', 'laptop', 'Mpnitor', 'keyboard', 'Mouse']

# quantity_laptop = devices.count('laptop')
                                
                                
# print(quantity_laptop)                                
                                
devices = ['phone', 'laptop', 'Mpnitor', 'keyboard', 'Mouse']

# devices.append('Tablet')               #add element

# devices.insert(2, 'washing machine')           #where i want to add

# print(devices)
                                
                                
                                
                              
devices = ['phone', 'laptop', 'Mpnitor', 'keyboard', 'Mouse']                               
                                
# print(devices.pop())                #remove element from back      
# print(devices)



# print(devices.remove('phone'))

# print(devices)



devices = ['phone', 'laptop', 'Mpnitor', 'keyboard', 'Mouse'] 

books = ['Harry Poter', 'Python for Beginners', 'The Tale of Two Cities']


# devices_books = devices + books

# devices_books = devices.extend(books)

# print(devices_books)
# print(devices)
# print(books)




# print(devices.sort())
# print(devices)


mixed_list = ['Elbe', 'Refrigerstor', 2024, 'Statue of Liberty', True, 1012.99, [1, 2, 3],'Germany']

# print(mixed_list)

# for i in mixed_list:

#     print(i)    


##################

#unpacking

numbers = [1, 2, 3, 4, 5]

# a, b, c, d, e = numbers
a, b, *c = numbers                 #*c rest value

# print(a)
# print(b)
# print(e)


# print(a)
# print(b)
# print(c)

num = [10, 20, 30]

def addition(a, b, c):
    return a + b + c

# print(addition(*num))




number_range = range(2, 6)

number_list = number_range

print(number_list)



