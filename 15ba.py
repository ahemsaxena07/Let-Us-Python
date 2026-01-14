#we have to calculate the sum of the age of the dogs present in pet dic. using funcation pro.
pet = {
    'dog': {
        'alex': 2,
        'ham': 4,
        'aje': 3
    },
    'cat': {
        'adj': 4,
        'xyz': 5,
        'abc': 6
    }
}
from functools import reduce #using .values() for taking values of name
add = reduce(lambda x , y: x + y, pet['dog'].values())
print(add)

#we can also do it by adding operator.add
from operator import add
lst = reduce(add, pet['dog'].values())
print(lst)

