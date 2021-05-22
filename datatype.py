# problem0
# listt = [1, 2, 3, 4, 5]
# print(len(listt))

# problem1
# list_ = [1, "2", 3.0]
# print(list_[0: 3])

# problem2
# list_ = [1, "2", 3.0, [4], (5)]
# print(list_[0: 5])

# problem3
''' Создать Лист из 5 разных имён.
    Создать пустую строку и через .join() соеденить пустую строку и все имена в списке'''
# list1 = ['isa', 'bek', 'ali', 'nur', 'bol']
# list2 = ","
# print(list2.join(list1))

# problem4
'''Создать 2 списка(List) заполнить данными, к первому списку добавить все объекты второго списка '''
# list1 = [1, 2.0]
# list2 = ["2", "3"]
# list1.extend(list2)
# print(list1)

# problem5
'''Взять Лист №1 из Google Colab и посчитать сколько раз там встречается имя "Jack"'''
# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack',
#          'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# print(names.count("Jack"))

# problem6
'''Удалить из Листа №1 объект "Jack"'''
# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack',
#          'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# names.remove('Jack')
# print(names)

# problem7
'''Создать пустой лист.
Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования'''
# a = []
# a.append('isa')
# a.append('2003 года рождения')
# a.append('python')
# print(a)

# problem8
'''Взять Лист №2 из Google Colab узнать индекс объекта(строки) "loop" и удалить его по индексу'''
# pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# print(pythonList.index('loop'))
# pythonList.pop(6)
# print(pythonList)

# problem9
'''Взять Лист №3 из Google Colab и посчитать произведение этих чисел т.е. умножить их все и вывести результат'''
# numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
# c = 1
# a = [6, 6, 2, 12, 10, 13, 9, 21, 15, 21, 3, 7]
# print('Произведение чисел:',end='')
# for i in a:c *= i
# print(i,'',end='')
# print('=',c)
'''НАДО РАЗОБРАТЬ!!!'''

# problem10
''' Взять строку №1
    создать два списка numbers и letters,
    пройтись по каждому элементу строки №1 и в numbers добавлять только числа, а в letters буквы '''
a = 'Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy',
'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon'
numbers = []
letters = []
