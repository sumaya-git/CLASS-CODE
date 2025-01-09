
# Understanding scope

# Global scope

global_var = 'This is a global variable.'

def outer_function():
    #Enclosing scope

    enclosing_var = 'This is an enclosing variable.'
     
    def inner_function():
        #Local scope

        local_var = 'This is a locaL variable.'

        # print(global_var)
        # print(enclosing_var)
        # print(local_var)


    inner_function()

outer_function()

# print('########################')

# print(global_var)




global_var = 'This is a global variable.'
# print(global_var)

def outer_function():
    #Enclosing scope

    enclosing_var = 'This is an enclosing variable.'
    global_var = 'This is a modified global variable'
     
    def inner_function():
        #Local scope

        local_var = 'This is a locaL variable.'
       

        inner_function()

outer_function()

# print(global_var)



# Assigning function to a variable


def square(num):
    return num**2

# print(square(4))


square_var = square

print(square_var(5))




















