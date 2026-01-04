portfolio = {
    'accounts': ['SBI', 'IOB'],
    'shares': ['HDFC', 'ICICI', 'TM', 'TCS'],
    'ornaments': ['10 gm gold', '1 kg silver']
}

# d = {'Mf': ['Reliance', 'ABSL']}
# combined = {**portfolio , **d}
# print(combined)

# portfolio['MF'] = ['Reliance', 'ABSL']
# print(portfolio)


# portfolio['accounts'] = ['Axis', 'BOB']
# print(portfolio)

del(portfolio['ornaments'])
print(portfolio)