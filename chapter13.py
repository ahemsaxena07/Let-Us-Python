# # # # # # # # # # # def print_it(i, j, *args, x, y, **kwargs):
# # # # # # # # # # #     print()
# # # # # # # # # # #     print(i, j, end = '')
# # # # # # # # # # #     for var in args:
# # # # # # # # # # #         print(var, end = '')
# # # # # # # # # # #     print(x, y, end = '')
# # # # # # # # # # #     for name, value in kwargs.items():
# # # # # # # # # # #         print(name, value, end = '')

# # # # # # # # # # # print_it(10, 20, x = 30, y = 40)
# # # # # # # # # # # print_it(10, 20, 100, 200, x = 30, y = 40)
# # # # # # # # # # # print_it(10, 20, 100, 200, x = 30, y = 40, a = 5, b = 6, c = 7)/

# # # # # # # # # # def fun(a, b = 100, c = 3.14):
# # # # # # # # # #     return a+b+c
# # # # # # # # # # w = fun(10)
# # # # # # # # # # print(w)
# # # # # # # # # # x = fun(20, 50)
# # # # # # # # # # print(x)
# # # # # # # # # # y = fun(30, 60, 6.28)
# # # # # # # # # # print(y)
# # # # # # # # # # z = fun(1, c = 3, b = 5)
# # # # # # # # # # print

# # # # # # # # # def print_it(a, b, c, d, e):
# # # # # # # # #     print(a, b, c, d ,e)
# # # # # # # # # lst = [10, 20, 30, 40, 50]
# # # # # # # # # tpl = ('A', 'B', 'C', 'D', 'E')
# # # # # # # # # s = {1, 2, 3, 4, 5}
# # # # # # # # # print_it(*lst)
# # # # # # # # # print_it(*tpl)
# # # # # # # # # print_it(*s)

# # # # # # # # def print_it(name = 'sanjay', marks = 75):
# # # # # # # #     print(name, marks)
# # # # # # # # d = {'name': 'Anil', 'marks': 50}
# # # # # # # # print_it(*d)
# # # # # # # # print_it(**d)

# # # # # # # def cal_sum_prod(x, y, z):
# # # # # # #     ss = x + y + z
# # # # # # #     pp = x * y * z
# # # # # # #     return ss, pp
# # # # # # # a = int(input('enter a: '))
# # # # # # # b = int(input('enter b: '))
# # # # # # # c = int(input('enter c: '))
# # # # # # # s, p = cal_sum_prod(a, b, c)
# # # # # # # print(s, p)
# # # # # # def ispangram(s):
# # # # # #     alphabet = set('abcdefghijklmnopqrstuvwxyz')
# # # # # #     return alphabet <= set(s.lower())
# # # # # # print(ispangram('the quick brown fox jumps over the lazy dog'))
# # # # # # print(ispangram('crazy fredrick bought many very exquisite opal jewels'))

# # # # # def convert(s1):
# # # # #     items = [s for s in s1.split('-')]
# # # # #     items.sort()
# # # # #     s2 = '-'.join(items)
# # # # #     return s2
# # # # # s = 'here-come-the-dots-followed-by-dashes'
# # # # # t = convert(s)
# # # # # print(t)

# # # # def generate_lst():
# # # #     lst = list()
# # # #     for i in range(1,21):
# # # #         lst.append((i, i**2, i**3))

# # # #     return lst
# # # # l = generate_lst()
# # # # print(l)

# # # def convert(s):
# # #     words = [word for word in s.split(' ')]
# # #     return ' '.join(sorted(list(set(words))))

# # # s = 'I felt happy because I saw the others were happy and because knew I should feel happy, but I want\'t really happy'
# # # t = convert(s)
# # # print(t)

# # # s = 'Sakhi was a singer because her mother was a singer, and sakhi\'s mother was a singer because her father was a singer'
# # # t = convert(s)
# # # print(t)

# # def count_alphbets_digits(s):
# #     d = {'digit': 0, 'alphabet': 0}
# #     for ch in s:
# #         if ch.isalpha():
# #             d['alphabet'] += 1
# #         elif ch.isdigit():
# #             d['digit'] += 1
# #         else:
# #             pass
# #     return(d)
# # d = count_alphbets_digits('james bond 007')
# # print(d)

# def frequency(s):
#     freq = {}
#     for word in s.split():
#         freq[word] = freq.get(word, 0) + 1
#     return freq
# sentence = 'It is true for all that that that that \
#     that that that refers to is not the same \
#         that that that refers to'
# d = frequency(sentence)
# words = sorted(d)
# for w in words:
#     print('%s:%d' % (w, d[w]))