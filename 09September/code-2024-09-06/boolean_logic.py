
# Boolean Logic

# AND, OR, NOT

# age = 23

# has_license = True

# if age > 18 and has_license:
#     print('you are allowed to drive.')



# age = 23

# has_license = False

# if age > 18 and has_license == True:    # True and False --> False
#     print('You are allowed to drive.')


# raining = False

# umbrella = True

# if raining == False or umbrella == True:    # True or True --> True
#     print('You can go outside.')



# if raining or umbrella:    # False or True --> True
#     print('You can go outside.')



# if True or False:                   # --> True
#     print('This will be True.')




# print(False or True) # -- True



# is_student = False

# if is_student:
#     print('Go to the field and play with your friends.')



# if not is_student:  # not False --> True
#     print('You need to pay the full price.')




# age = 14

# parent_permission = True


# if age >= 16 or (age >= 12 and parent_permission):  # False or (False and True) --> False or False --> False
    
#     print('You can skydive.')



# age = 14

# parent_permission = True


# if age >= 16 or (age >= 12 and not parent_permission):  
    
#     print('You can skydive.')



# temperature = 25

# humidity = 50

# condition = 'cloudy'

# wind_speed = 37

# # if temperature >= 20 and humidity >= 30 and condition == 'windy':
# #     print('strom coming')



# if temperature >= 20 and (humidity <= 30 and condition == 'windy') and not wind_speed ==50:
#     print('strom coming')



# Short-circuiting

def watch_sport():
    print('Watiching sports is my favourite activity in the weekends.')
    return True


def is_weekend():
    print('Today is saturday.')
    return False

# watch_sport() or is_weekend()

# is_weekend() and watch_sport()


if watch_sport() and not is_weekend():
    print('Lunch')



