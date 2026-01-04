def palin(n):
    if n != str:
        return False
    if n[0:] == n[:-1]:
        return palin(n == True)
    if n[1:1:] == n[:1:-2]:
        return palin(n == True)
    else:
        return False

words = input('enter a word: ')
isit = palin(words)
if isit == True:
    print(f"the {isit} is palindrome")
else:
    print(f'the {isit} is not palindrome')