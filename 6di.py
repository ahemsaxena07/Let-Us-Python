i = 1
while i <= 10:
    r = float(input("enter annual rate: "))
    q = float(input("enter the simple interest: "))
    p = float(input("enter the principal p compounds: "))
    n = int(input("enter years: "))
    a = p * (1 + r / q) ** (n * q)
    print("amount:", a)
    i = i + 1
              