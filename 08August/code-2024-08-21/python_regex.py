
import re

text = 'We went to sunmoon restaurant yesterday.We enjoyed a lunch there and took some rest'

# result = re.search('went', text)

# result = re.search('res\w*', text)

# print(result)   #ooutput: <re.Match object; span=(3, 7), match='went'>

# print(result.group())



# text = 'We went to sunmoon restaurant yesterday.We enjoyed a lunch there and took some rest'

# result = re.findall('r\w*', text)

# print(result)


import re

text = 'You can wrap texts in VS code by pressing Alt+Z'

# result = re.match(r'wrap', text)    #r = raw string
# print(result)

# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.fullmatch(r'You can wrap texts in VS code by pressing Alt+Z.', text)
# print(result)


text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.fullmatch(r'.*', text)            # .* = * take all sentences 
# print(result)



# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.split(r'in', text)            # .* = * take all sentences 
# print(result)            #['You can wrap texts ', ' VS code by press', 'g Alt+Z.']



# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.split(r'in', text, maxsplit=1)            # .* = * take all sentences 
# print(result)       #['You can wrap texts ', ' VS code by pressing Alt+Z.']




# text = 'You can wrap texts in VS code by pressing Alt+Z.'

# result = re.sub(r'in', 'on', text,)            # sub= replace in to on 
# print(result)      #You can wrap texts on VS code by pressong Alt+Z.



text = 'You can wrap texts in VS code by pressing Alt+Z.You can wrap texts in VS code by pressing Alt+Z.You can wrap texts in VS code by pressing Alt+Z.'

# result = re.sub(r'in', 'over', text,count=3)            
# print(result)



text = 'You can wrap texts in VS code by pressing Alt+Z.'


result = re.finditer(r'\b\w{4}\b', text)               # any type of match it will find
# print(result)       #<callable_iterator object at 0x7b91ee28bc10>

# for item in result:
#     print(item)              # <re.Match object; span=(8, 12), match='wrap'><re.Match object; span=(25, 29), match='code'>      


# print(list(result))



# for item in result:
#     print(item.span())     

