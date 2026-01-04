# my code
# for i in range(0, 301):
#     if i % 2 != 0:
#         if i % 3 != 0:
#             print(i)

# using for loop-simple logic
for i in range(2, 301):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
        break

    if is_prime:
        print(i)
    