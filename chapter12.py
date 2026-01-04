# # # # # # # d = {'a': 1, 'b': 2,'c':3, 'd':4}
# # # # # # # d1 = {k: v ** 3 for (k,v) in d.items()}
# # # # # # # print(d1) 

# # # # # # # d2 = {k: v ** 3 for (k,v) in d.items() if v > 3}
# # # # # # # print(d2)

# # # # # # # d3 = {k: ('Even' if v % 2 == 0 else 'odd') for (k,v) in d.items()}
# # # # # # # print(d3)

# # # # # # # arr = [[1,2,3], [4,5,6], [7,8,9]]
# # # # # # # c = [*arr[0], *arr[1], *arr[2]]
# # # # # # # print(c)

# # # # # # # # lst = [num for num in range(2,50) if num % 2 ==0 and num % 4 == 0]
# # # # # # # # print(lst)

# # # # # # mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# # # # # # a = [num for lst in mat for num in lst]
# # # # # # print(a)

# # # # # import random
# # # # # r = {int(15 + 30 * random.random( )) for num in range(10)}
# # # # # print(r)
# # # # # count = len({num for num in r if num < 30})
# # # # # print(count)
# # # # # s = {num for num in r if num < 30}
# # # # # r = r - s 
# # # # # print(r)

# # # # lst = [(), (), (10), (10, 20), ('',), (10,20,30), (40,50), (), (45)]
# # # # lst = [tpl for tpl in lst if tpl]
# # # # print(lst)

# # # s1 = 'dreams may change, but freinds are forever'
# # # s2 = [''.join(w.capitalize() for w in s1.split())]
# # # s3 = s2[0]
# # # print(s3)

# # words = {'tub': 1, 'toothbrush': 2, 'towel': 3, 'nailcutter': 4}
# # d = {''.join(alpha for alpha in k if alpha not in 'aeiou'):v for (k,v) in words.items()}
# # print(d)

# # mat1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# # mat2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# # mat3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# # for i in range(len(mat1)):
# #     for j in range(len(mat1[0])):
# #         mat3[i][j] = mat1[i][j] + mat2[i][j]
# # print(mat3)
# # mat3 = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
# # print(mat3)

# mat1 = [[3,43, 53, 23], [4343,5343,934,3343]]
# mat2 = [[33,2,59,342], [534,9530,348,3944]]
# mat3 = [[0,0,0,0], [0,0,0,0]]
# mat3 = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
# print(mat3)

emp = {
    'A101' : {'name': 'Ashish', 'age': 30, 'salary': 21000},
    'B102' : {'name': 'Dinesh', 'age': 25, 'salary': 12200},
    'A103' : {'name': 'Ramesh', 'age': 28, 'salary': 11000},
    'D104' : {'name': 'Akheel', 'age': 30, 'salary': 18000}
}

d1 = {k:v for (k,v) in emp.items() if k.startswith('A')}
d2 = {k:v['name'] for (k,v) in emp.items()}
d3 = {k:v['age'] for (k,v) in emp.items()}
d4 = {k:v['age'] for (k,v) in emp.items() if v['age'] > 30}
d5 = {k:v['name'] for (k,v) in emp.items() if v['name'].startswith('A')}
d6 = {k:v['salary'] for (k,v) in emp.items() if v['salary'] > 13000 and v['salary'] <= 20000}
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)