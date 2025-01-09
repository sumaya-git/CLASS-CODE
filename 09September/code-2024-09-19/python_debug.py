
# Debugging in Python 


def divide(a, b):
    return a / b
# print(divide(10 , 5))



def calculate_average(numbers):
    total = 0

    for i in numbers:
        total += i
    
    average = total / len(numbers)

    return average


num_list = [10, 50, 20, 70, 30, 40]

print(calculate_average(num_list))






