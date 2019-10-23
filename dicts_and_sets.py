# # key can be any immutable values, while values can ba any type of values
# my_fruit_counter = {}
# my_fruit_counter["banana"] = 5
# my_fruit_counter["fig"] = 1
# my_fruit_counter["orange"] = 10
# my_fruit_counter["apple"] = 3

# print(my_fruit_counter)
# print(my_fruit_counter.keys())
# print(list(my_fruit_counter.keys()))
# print(my_fruit_counter.values())
# print(list(my_fruit_counter.values()))
# print(my_fruit_counter.items())
# print(list(my_fruit_counter.items()))

# print(sorted(my_fruit_counter.items()))

# fruits_by_count = sorted(
#     my_fruit_counter.items(),
#     key=lambda x: x[1],
#     reverse=True
# )

# print(fruits_by_count)

# my_food_type = {
#     'vegetables': [],
#     'meats': [],
#     'fruit': []
# }

# print(my_food_type)

# my_food_type['vegetables'].append('celery')
# my_food_type['vegetables'].append('zucchini')
# my_food_type['vegetables'].append('carrot')

# print(my_food_type)

# for food in my_food_type['vegetables']:
#     food = 'bubblegum'
#     print(food)


# print(my_food_type)

# for i in range(len(my_food_type['vegetables'])):
#     my_food_type['vegetables'][i] = 'bubblegum'
#     print(my_food_type['vegetables'][i])

# print(my_food_type)


# my_veg_set = set()

# my_fruit_set = {'banana', 'fig', 'grapefruit'}


# def check_for_fruit(fruit, fruit_set):
#     if fruit in fruit_set:
#         print("We have a", fruit)
#     else:
#         print("We don't have a", fruit)


# check_for_fruit('banana', my_fruit_set)
# check_for_fruit('peach', my_fruit_set)

# my_fruit_set.add('peach')
# check_for_fruit('peach', my_fruit_set)

# my_fruit_set.remove('banana')
# check_for_fruit('banana', my_fruit_set)

print({1, 2, 3} == {2, 1, 3})
print({1: 1, 2: 2, 3: 3} == {2: 2, 1: 1, 3: 3})
