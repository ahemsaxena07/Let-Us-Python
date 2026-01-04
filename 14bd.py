def tab(n, count = 0, result = ""):
    if count >= len(n):
        return result 
    if n[count] == '\t':
        return tab(n, count + 1, result)
    else:
        return tab(n, count + 1, result + n[count])
text = input('enter a sentence: ')
total = tab(text)
print(f'final sentence: {total}')