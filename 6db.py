lst = ["desert", "dessert", "to", "too", "lose", "loose"]
s = "Mumbai"
i = 0
for ele in lst:
    if len(lst) > i:
        if i > 3:
            break
        else:
             print(i, lst[i], s[i])
             i +=1 

# lst = ["desert", "dessert", "to", "too", "lose", "loose"]
# s = "Mumbai"
# i = 0
# while i < len(lst):
#     if i > 3:
#         break
#     else:
#         print(i, lst[i], s[i])
#         i += 1