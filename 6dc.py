i = 'Nagpur-440010'
alphacount = 0
digitcount = 0
for ch in i:
    if ch.isalpha():
        alphacount += 1
    elif ch.isdigit():
        digitcount+= 1
print("Alphabets: ", alphacount)
print("Digits: ", digitcount)