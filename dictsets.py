# s = set()
# print(type(s))
# s.add('qwerty')
# print(s)
# s.clear()
# print(s)

# x = {'a', 'b', 'c'}
# y = {'a', 'd', 'e', 'f'}

# z = x.intersection(y)
# print(z)

# z = x.difference(y)
# print(z)

# c = {   'key1': 1,
#         'key2': 2,
#         'key3': '3',
#         2 : 'adf'}
# print(c)

# problem0
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# a = dates_of_birth.remove(7)
# print(a)

# problem1
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# a = farm_1.intersection(farm_2)
# print(a)

# problem2
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# a = farm_2.difference(farm_1)
# print(a)

# problem3
# set1 = {12, '9', 'bomb', 0, 'sfvsdf'}
# a = set1.add('blablabla')
# print(set1)

# problem000
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_barmak'] = 130
# print(menu)
# menu.update({'besh_barmak': 135})
# print(menu)
# menu.pop('borsh')
# print('Ваш повар отвратительно готовит борщ')
# print(menu)

# problem10
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
# print(menu)

# problem020
# sets = {'add', 'update', 'intersection', 'difference', 'remove',
#         'pop', 'clear', 'discard', 'intersection_update'}
# dicts = {'clear', 'keys', 'get', 'items', 'update', 'values'}
# a = sets.intersection(dicts)
# print(a)

# problem31
'''Создайте пустой словарь.
Запустите цикл который 3 раза спросит его имя и его пароль.
Записывайте имя пользователя как ключ, а пароль как его значение.'''
# a = {}
# i = 0
# while i < 3:
#  i = i+1
#  c = input('Name: ')
#  s = input('Password: ')
#  a[c] =s
#  print(a)

# problem27
# dicts = {'isa': 'Программист', 'Malika': 'Мастер Парикмахер',
#          'Bekbol': 'футболист', 'aika': 'doctor', 'nurik': 'стоматолог'}
# for a,b in dicts.items():
#     print(f'Здраствуйте {a}, {b} прекрасная профессия')

# problem22
# a = set()
# i = 0
# while i < 10:
#     i = i + 1
#     c = int(input('enter num: '))
#     s = a.add(c)
#     print(a)

# problem11
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
#     'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# a = set(south_american_countries)
# print(list(a))

# problem101
# a = ['Купальник', 'Зонт', 'Полотенце', 'Крем от заг', 'настроение']
# a = []
# i = 0
# while i < 5:
#     i = i + 1
#     c = input('вещи: ')
#     a.append(c)
# print(a)

# problem001
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = set()
# a = farm_1.intersection(farm_2)
# farm_3.update(a)
# print(farm_3)

# problem100
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = set()
# a = farm_2.difference(farm_1)
# farm_3.update(a)
# print(farm_3)