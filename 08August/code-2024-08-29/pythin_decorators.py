
# Creating simple decoratos

# def decarator(func):
#     def wrapper():
#         print(f'Sky is the limit.')
#         func()
#         print(f'Oceans are below the Earth.')
#     return wrapper



# def display_text():
#     print(f'Mountains are on the ground.')

# display_text()





# def decorator(func):
#     def wrapper():
#         print(f'Sky is the limit.')
#         print(f'Oceans are below the Earth.')
#         return func()
#     return wrapper



# def display_text():
#     return (f'Mountains are on the ground.')


# new_text = decorator(display_text)

# print(new_text())




def decorator(func):
    def wrapper():
        print(f'Sky is the limit.')
        func()
        print(f'Oceans are below the Earth.')
     
    return wrapper


def display_text():
    print(f'Mountains are on the ground.')


# new_text = decorator(display_text)

# print(new_text())




# def decorator(func):
#     def wrapper():
#         print(f'Sky is the limit.')
#         func()
#         print(f'Oceans are below the Earth.')
     
#     return wrapper

# @decorator           # @ = argument
# def display_text():
#     print(f'Mountains are on the ground.')

# display_text()




# def decorator(func):
#     def wrapper(which,where):
#         print(f'Sky is the limit.')
#         func(which,where)
#         print(f'Oceans are below the Earth.')
     
#     return wrapper

# @decorator
# def display_text(which, where):
#     print(f'Mountains are on the ground.{which} is the tallest mountain. It is situated in {where}.')

# display_text('Everst', 'Nepal')




# def decorator(func):
#     def wrapper(*args,):
#         print(f'Sky is the limit.')
#         func(*args)
#         print(f'Oceans are below the Earth.')
     
#     return wrapper

# @decorator
# def display_text(which, where):
#     print(f'Mountains are on the ground.{which} is the tallest mountain. It is situated in {where}.')

# display_text('Everst', 'Nepal')




# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print(f'Sky is the limit.')
#         func(*args, **kwargs)
#         print(f'Oceans are below the Earth.')
     
#     return wrapper

# @decorator
# def display_text(which, where, who='Edmund Hillary'):
#     print(f'Mountains are on the ground.{which} is the tallest mountain. It is situated in {where}. {who} is the first human climbed on top of it.')

# display_text('Everst', 'Nepal', who='Tenzing Norgay')


    


# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print(f'Sky is the limit.')
#         func(*args, **kwargs)
#         print(f'Oceans are below the Earth.')
     
#     return wrapper

# @decorator
# def display_text(which, where, who='Edmund Hillary'):
#     print(f'Mountains are on the ground.{which} is the tallest mountain. It is situated in {where}. {who} is the first human climbed on top of it.')


# decorator(display_text())
# display_text('Everst', 'Nepal', who='Tenzing Norgay')




# def apply_discount(func):
#     def wrapper(*args, **kwargs):
#         total_price = func(*args, **kwargs)

#         return total_price - 70
#     return wrapper



# @apply_discount
# def calculate_total_price(price, quantity):
#     return price * quantity

# print(calculate_total_price(100, 3))





# def apply_discount(discount):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#              total_price = func(*args, **kwargs)

#              return total_price - discount
#         return wrapper
#     return decorator
    



# @apply_discount(30)
# def calculate_total_price(price, quantity):
#     return price * quantity

# print(calculate_total_price(100, 3))


# add more value------->

# def apply_discount(discount, tax):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#              total_price = func(*args, **kwargs)

#              return total_price - discount + tax
#         return wrapper
#     return decorator
    



# @apply_discount(30, 50)
# def calculate_total_price(price, quantity):
#     return price * quantity

# print(calculate_total_price(100, 3))


# add multiple decorator----->






def text_upper(func):
    def wrapper(*args, **kwargs):
        text =  func(*args, **kwargs)
        return text.upper()
    return wrapper


def text_lower(func):
    def wrapper(*args, **kwargs):
        text =  func(*args, **kwargs)
        return text.lower()
    return wrapper

def text_capitalize(func):
    def wrapper(*args, **kwargs):
        text =  func(*args, **kwargs)
        return text.capitalize()
    return wrapper

@text_capitalize
@text_upper
@text_lower
def greet():
    return f'weLcoMe to pyThoN deCorAtoRs.'


print(greet())
