i = 1
while i <= 3:
    j = 1
    while j <= 3:
        k = 1
        while k <= 3:
            if i == j and j == k and k == i:
                k += 1
                continue
            else:
                print(i, j, k)

            k += 1
        j += 1
    i += 1