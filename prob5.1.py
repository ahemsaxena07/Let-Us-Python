qty = int(input("enter the quantity: "))
price = float(input("enter the price: "))
if qty > 1000:
    dis = 10
else:
    dis = 0

texp = qty * price - qty * price * dis/100
print(f"the total expense is {texp}")