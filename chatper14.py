# # # def generate(n):
# # #     lol = [[] for i in range(n ** n)]
# # #     pos = 0
# # #     for i in range(1, n + 1):
# # #         for j in range(1, n + 1):
# # #             for k in range(1, n + 1):
# # #                 t = [i,j,k]
# # #                 lol[pos] = t
# # #                 pos += 1
# # #     return lol
# # # print(generate(4))

# # def factorize(n, i):
# #     if i <= n:
# #         if n % i == 0:
# #             print(i, end=',')
# #             factorize(n // i, i)  
# #         else:
# #             factorize(n, i + 1)
# # num = int(input('enter a number: '))
# # print("prime factors are: ")
# # factorize(num, 2)

# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + sum_of_digits(n // 10)
# num = int(input('enter a positive number: '))
# result = sum_of_digits(num)
# print(f"sum of digits of {num} is: {result}")
# head recursion 
# def number(s):
#     if s == 0:
#         return 0
#     else:
#         n = s + number(s - 1)
#         return n 
# max = int(input("enter the number: "))
# source = number(max)
# print(f"the sum of first five number: {source}")
# tail recursion
def sum(f, accumulator = 0):
    if f == 0:
        return accumulator
    else:
        return sum(f - 1, accumulator + f)
sumof = int(input('enter a number: '))
max = sum(sumof)
print(max)


