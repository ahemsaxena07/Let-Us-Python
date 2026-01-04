
prices = {
    'apple' : 70,
    'milk': 20,
    'bread': 35,
    'eggs': 8
}

quantity = {
    'apple': 5,
    'milk':2,
    'bread':1,
    'eggs': 10
}

for g1 in prices, quantity:
    g1 = prices.values(['apple']) + quantity.values(['apple'])
print(g1)


