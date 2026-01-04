# awaitleimport operator 
# lst = ['dhoni', 'sachin', 'virat', 'raina']
# d = dict.fromkeys(lst, 50)
# print(len(lst))
# print(len(d))
# print(d)
# -------------------------------------------------------
# d = {'oil': 230, 'clip': 343, 'stud': 175, 'nut': 35}
# print('original dictionary: ', d)

# d1 = sorted(d.items( ))
# print('Asc. order by key: ', d1)
# d2 = sorted(d.items( ), reverse = True)
# print('Asc, order by key: ', d2)

# d1 = sorted(d.items(), key = operator.itemgetter(1))
# print('Asc. order by values: ', d1)
# d2 = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
# print('Dsc. order by values: ', d2)
# -----------------------------------------

# d1 = {'kiwi': 70, 'mango':45}
# d2 = {'apple': 60, 'banana': 20}
# d3 = {'guava': 55, 'pineapple': 50}
# d4 = {}
# for d in (d1, d2, d3):
#     d4.update(d)
# print(d4)

# d5 = {**d1, **d2, **d3}
# print(d5)

# d6 = list({*d1, *d2, *d3})
# print(d6)

# --------------------------------------

# d1 = {'ahem': 34,'aman': 343, 'heleo':534}
# if bool(d1):
#     print('dictionary is not empty')

# d2 = {}
# if not bool(d2):
#     print('dicitonary is empty')
# ----------------------------------------

# d = {
#   'anil': {'salary': 70000, 'age': 30},
#   'alak pandey': {'salary': 340000, 'age': 455},
#   'hehe': {'salary': 13000, 'age': 45}
# }

# lst = []
# for v in d.values():
#     lst.append(v['salary'])

# print(max(lst))
# print(min(lst))

# ---------------------------------------

students = {440: 'ass', 239: 'boobs', 600: 'back'}
rollno = int(input("enter the roll no.: "))
name = students.get(rollno, 'students')
print(f'Congratulations {name}')
rollno = int(input("Enter the roll no.: "))
name = students.get(rollno, 'students')
print(f'Congratulations {name}')