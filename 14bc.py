def vowel(n, count = 0):
    if count >= len(n):
        return 0
    words = 'aeiouAEIOU'
    if n[count] in words:
        return 1 + vowel(n, count + 1)
    else:
        return vowel(n, count + 1)
text = str(input('enter a word: '))
total = vowel(text)
print(f'number of vowels in word: {total}')