

# Function defination/ structure

# Function with no argument

def greet(): # Header
    '''This is a sinple function that greets people ''' # Documatation string(doc string)
    text = 'Hello everyone,good afternoon.'  # Body

    return text # return
# Call/ use function

# print(greet())


# Function with argument


def calculate_total_price(price,quantity):  #' price, quantity--> parameters'
    '''This function calculates the total price of a product'''

    total_price = price * quantity

    return total_price
# print(calculate_total_price(20, 5))   #20, 5 --> arguments





def calculate_total_price(price,quantity):  #' price, quantity--> parameters'
    '''This function calculates the total price of a product'''

    total_price = price * quantity

    return f'The total price is {total_price}.'
# print(calculate_total_price(20, 5))





def calculate_area(lenth, width):
    '''Returens the area of arectangle'''
    area = lenth * width

    return area

calc_area = calculate_area(10,2)

# print(calc_area)
   


# Function returinf multiples values

def get_max_min(num_list):
    '''Returns the maximum and minimum values from a list'''

    maximun = max(num_list)
    minimum = min(num_list)

    return maximun, minimum

num_max, num_min = get_max_min([30, 100, 70, 50, 77, 80])

# print(num_max)
# print(num_min)


# print(get_max_min([30, 100, 70, 20, 77, 80]))


numbers = [2034, 300, 450, 1006, 1200, 3, 90, 180]

# print(get_max_min(numbers))


# Input packed/unpacked data

# def calculate_bmi(weight, height, age):
#     '''Returns Body-mass index based on given data'''

#     bmi_index = weight/ height**2

#     return bmi_index

# print(calculate_bmi(62, 1.70, 32))




def calculate_bmi(*args):
    '''Returns Body-mass index based on given data'''

    bmi_index = (args[0] / args[1]**2) /100

    return bmi_index

# print(calculate_bmi(62, 1.70, 32))


data_list = [62, 0.170, 32]

# print(calculate_bmi(*data_list))



# Function as an argument

# def calculate_total_price(price, quantity):
#     total_price = price * quantity
#     return total_price


# def calculate_total_price_with_discount(func, price, quantity, discount):

    

#     total_value = func(price, quantity)
#     discount_value = total_value * ( discount/ 100)
#     return total_value - discount_value


# print(calculate_total_price_with_discount(calculate_total_price, 100, 3, 30))




# def get_multiplication(factor):

#     def multiply_by_three(num):
#         num = factor
#         return num * 3
    
#     return multiply_by_three(factor)
    
    
# print(get_multiplication(100))


# passing arguments in inner function

# def get_multiplication(factor):

#     def multiply_by_three(num):
#         return num * factor
    
#     return multiply_by_three

# outer_func = get_multiplication(7)
# print(outer_func(100))


# keyword arguments

# def greet(name):
#     print(f'Hello {name}, Good morning')

# greet('Alex')


def greet(name='Emily'):
    print(f'Hello {name}, Good morning')

# greet()
# greet('Alex')



def greet(name, age=40):
    print(f'Hello {name}, Good morning. He is {age} years old.')

greet('Jordan',age=30)

def greet(name, age=40, **kwargs):
    print(f'Hello {name}, Good morning. He is {age} years old.')
    print('He is studying:')
    for item in kwargs['subject']:
        print(item)

greet('Jordan',age=30, height=175, weight=70, is_student=True, subject=['math', 'Physics', 'Programming'])



