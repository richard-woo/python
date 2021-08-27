#!/usr/bin/env python
#list function
food = ['apple', 'bananas', 'tofu', 'cats']
def listPractice(para):
    #para.insert(-1, 'and')
    food[-1] = 'and ' + food[-1]
    string = ''
    for i in range(len(para)):
        string += str(para[i])
        if i < len(para) - 1:
            string += ','

    return string

print(food)
print(listPractice(food))
print(food)

