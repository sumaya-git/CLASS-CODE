

# def simple(*args, **kwargs):


name = 'Alex'

# new_name = name*5
# new_name = ((name + ' ')*5)

# print(new_name)
# def text_convert(name):
#     full_text = name + ' 5 ' + str(True)
#     return full_text


# print(text_convert('Emily'))
# print(text_convert('Thomas'))

#string slicing

# text = 'Far across the distance'

# print(text(4))

# print(text[0:10:3])


     # - is revers direction


# print(text[-11])

# print(len(text))
# print(text[22])

# print(text[-1:-10:-1])

# print(text[::-1])


#strip method


# text = '            Far across the distancespaces between us           '


# new_text = text.strip()

# new_text = text.lstrip() + 't'

# print(text)
# print(new_text)


#string format
# text = 'Lunch time is %s passed until %d.'

# new_text = text % ('already' , 12)


# print(text)
# print(new_text)


# text = 'The {} was really good. Now i just need to {}.'

# new_text = text. format('dinner', 'rest')
# print(text)
# print(new_text)



# f-string

# day = 'Friday'
# num = 5


# text = f'{day.upper()} is the {num} day before weekend.'
# print(text)


# def count_string(txt, sub_txt):

#     count_num = txt.count(sub_txt)

#     result = f'We found{sub_text} inside the original text{count_num} times.'

#     return result

# text = 'We are almost done with the lesson'

# sub_text = 'a'

# x = count_string(text, sub_text)

# print(x)



def weekday():
    day = input('Enter a weekday: ')

    num = input('Enter day number: ')
    text = f'{day.capitalize()} is the {num}th day of the week. ' + f'Saturday comes after Friday.'

    return text

print(weekday())




