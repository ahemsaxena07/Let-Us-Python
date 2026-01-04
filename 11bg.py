marks = {
    'subu': {'maths': 88, 'eng': 60, 'sst': 95},
    'amol': {'maths': 78, 'eng': 68, 'sst': 89},
    'raka': {'maths': 56, 'eng': 66, 'sst': 77}
}
amol = marks['amol']
print(amol.get('eng'))


marks['raka']['maths'] = 77
print(marks['raka'])

names = sorted(marks.items())
print(names)

