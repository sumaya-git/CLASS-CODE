
# Try & Except

# result = 100/2
# print(result) 

'''
50.0
'''

# result = 100/0
# print(result)
'''
ZeroDivisionError: division by zero
'''


# try:
#     result = 100/2
#     print(result)
# except:
#     print('This is coming from except block.')

# print('The end')

'''
50.0
The end
'''

# try:
#     result = 100/0
#     print(result)
# except:
#     print('This is coming from except block.')

# print('The end')

'''
This is coming from except block.
The end
'''

# try:
#     result = 100 / 0
#     print(result)
# except:
#     result = 100 / 20
#     print(result)
#     print('This is coming from except block.')


# print('The end')

# try:
#     result = 100 / 0
#     print(result)
# except:
#     result = 100 / 20
#     print(result)
#     print('This is coming from except block.')


# print(f'The result is {result}')


# try:
#     result = 100/ 2
# except: 
#     result = 100/100

# print(result)  



# try:
#     result = 100/ 0
# except Exception as e:
#     print(e) 
#     result = 100/100

# print(result) 


# try:
#     result = 100/ 0
# except ZeroDivisionError as err:
#     print(err) 
#     result = 100/100

# print(result) 




# try:
#     num = int(input('Enter number: '))
#     result = 100/ num
#     print(result)
# except ZeroDivisionError as err:
#     print(err) 
#     result = 100/100



# import builtins       # find error

# print(dir(builtins))


# try:
#     num = int(input('Enter a number: '))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)
# except Exception as err:
#     print(err)


# keyboardInterrupt

# try:
#     num = int(input('Enter a number: '))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)
# except KeyboardInterrupt as krr:
#     print(krr)
# except Exception as err:
#     print(err)
# finally: 
#     print('This is the end finally')




# def check_age(age):
#     return f'I am {age} yeras old'

# print(check_age(31))




# def check_age(age):
#     if age <= 0:
#         raise Exception
#     return f'I am {age} yeras old'

# print(check_age(-25))




# def check_age(age):
#     if age <= 0:
#         raise Exception('Age must be a positive number')
#     return f'I am {age} yeras old'

# # print(check_age(-25))


# try:
#     print(check_age(25))
# except Exception as e:
#     print(e)











