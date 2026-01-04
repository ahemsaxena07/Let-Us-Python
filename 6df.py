for i in range(0, 501):
    digits = [int(d) for d in str(i)]
    sum_of_cubes = sum(d ** 3 for d in digits)
    if i == sum_of_cubes:
        print(i)
