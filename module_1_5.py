# Lesson tuple & lists

immutable_var = (0, 'текст', False, 1.2)
print(immutable_var)
# immutable_var [0] = 3
# >>> TypeError: 'tuple' object does not support item assignment - кортеж не поддерживает изменение элементов
mutable_list = [1, 2, 'неизменяемые', 'слово', 'кредо', False, 'or', True]
mutable_list [0] = 3
mutable_list [1] = 4
mutable_list [3] = 'слова'
mutable_list [5] = True
mutable_list [7] = False
print(mutable_list)