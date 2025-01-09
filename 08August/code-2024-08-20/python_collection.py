
# Iterables
# any() , all() returns true or false

# a_list =['Painiting', 2024, True, {'price':33.99}, 3+5j, 'Mercedes']

a_list =['Painiting', 2024,'', True, {'price':33.99}, 3+5j, 'Mercedes']



# print(any(a_list))

# print(all(a_list))

another_list = ['',[], False,0, 'Garding']

# print(any(another_list))
# print(all(another_list))


# collections module

import collections as c

hobbies = ['Photography', 'Travelling', 'Hiking', 'Cooking', 'Yoga', 'Reading', 'Fishing']

# print(len(hobbies))
hobbies_counter = c.Counter(hobbies)
# print(hobbies_counter)

# print(hobbies_counter['Travelling'])

# for item in hobbies_counter:
#     print(item)


for item in hobbies_counter.keys():
    print(item)

print('-'*30)

for item in hobbies_counter.values():
    print(item)

print('-'*30)
for item in hobbies_counter.items():
    print(item)


print('-'*30)

# print(hobbies_counter.total())

print('-'*30)

# print(hobbies_counter.most_common(3))

# for item in hobbies_counter.most_common():
#     print(item)


# counter object

profession = c.Counter(Engineers = 3, Developers = 10, Programmers = 20)
# print(profession)



hobbies = ['Photography', 'Traveling', 'Yoga', 'Hiking', 
           'Cooking', 'Yoga', 'Reading', 'Fishing', 'Yoga', 'Cooking']

hobbies_counter = c.Counter(hobbies)

profession = ['Engineers', 'Developers', 'Programmers', 'Testers', 'Photography']

profession_counter = c.Counter(profession)

# print(profession_counter)

combine = hobbies_counter + profession_counter
# print(combine)


# combine = hobbies_counter.update(profession_counter)
reduce = hobbies_counter.subtract(profession_counter)

# print(combine)
# print(reduce)
# print(hobbies_counter)


# orderdDict()

website_config = {
    'name': 'python',
    'url': 'https://python.org',
    'office': 'Silicon valley 107',
    'ssl': 'Letsencrypt'

}

od = c.OrderedDict(website_config)
# print(website_config)
# print(od)
# print(type(od))

# print(od['name'])

# print(od.move_to_end('url'))



# chainMap()

dict_1 = { 
    'name': 'python',
    'url': 'https://python.org',
    'office': 'Silicon valley 107',
    'ssl': 'Letsencrypt'
    }

dict_2 ={ 
    'name': 'Regex',
    'url': 'https://regexlearn.com',
    'office': 'California 373',
    'ssl': 'Letsencrypt'
    }

chain_dict = c.ChainMap(dict_1,dict_2)

# print(chain_dict['name'])

# print(chain_dict.maps)

# print(chain_dict.maps[1])


# print(chain_dict.maps[1]['ssl'])

# namedtuple()

coordinate = c.namedtuple('Location', ['lattitude', 'longitude'])

place = coordinate(34.55, 120.77)
print(place)









