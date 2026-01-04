print("enter the string:")
text = input()

freq_dict = {}

for char in text:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1

print("\n character freq dictionary:")
print(freq_dict)

print("\n character freq histogram:")
print("-" * 40)

for char in freq_dict:
    if char == " ":
        display_char = 'space'
    else:
        display_char = char 
        
    bar = '*' * freq_dict[char]
    print(f"{display_char} : {bar}({freq_dict[char]})")

print("-" * 40)