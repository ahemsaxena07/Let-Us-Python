import functools
lst = ['Benevolent', 'Dictator', 'For', 'Life']
final = functools.reduce(lambda x, y: x + ' ' + y, lst)
print(final)