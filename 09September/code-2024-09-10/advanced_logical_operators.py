

# XOR 

a = True

b = False

result = (a or b) and not (a and b)

print(result)


'''
-->(True or False) and not (True and False)
--> True and not False
--> True and True
--> True

'''

# NAND


a = True

b = False

result = not (a and b)

'''
--> not (True and False)
--> not False
--> True

'''

print(result)


# NOR

a = False

b = False


result = not (a or b)

'''
--> not (False or False)
--> not False
--> True
'''

print(result)


def nor_func(a, b):
    return not (a or b)

print(nor_func(True, True))





