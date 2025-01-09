
# # Recursive Functiuon

# def recursive_function(parameters):  # Header
#     # Base case 
#     if condition:
#         # Condition to end the recursion
#         return default value
#     # recursive case
#     else:
#         return recursive_function(modified_parameters)



#---------------->

# sum up all the numbers untill a specific number.
# guven_number = 10 -->0 + 1 + 2 + 3,........+10 = 55


# print(sum(range(11)))

# def recursive_sum(n):
#     if n ==0:
#         return 0
#     else:
#         return n + recursive_sum(n - 1)


# print(recursive_sum(5))




# ass all element from a given list of numbers.



# def recursive_addition(lst):
#     if not lst:
#         return 0
    
#     else:
#         return lst[0] + recursive_addition(lst[1:])
   

# numbers = [3, 5, 2, 7]

# result = recursive_addition(numbers)
# print(result)



# Reversed a string from a given string using recursive function



# def rev_txt(txt):
#     if txt == '':
#         return ''
#     else:
#         return txt[-1] + rev_txt(txt[:-1])
    

# given_text = 'The Last of Us'

# reversed_line = rev_txt(given_text)

# print(reversed_line)


# Reversed a list from a given list using recursive function

# numbers = [3, 5, 2, 7] # --> [7, 2, 5, 3]


# def rev_list(num):
#     if num == []:
#         return num
#     else:
#         return [num[-1]] + rev_list(num[:-1])


# print(rev_list(numbers))



# factorial: 3! = 3*2*1 = 6

# create a recursive function to calculate its factorial

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1) 


print(factorial(10))
















