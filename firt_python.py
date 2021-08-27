#!/usr/bin/env python
#This program says hello and asks for my age

import sys
print('hello word')

v = input()
def testFunction(para):
	if para == 1:
		print('Right!')
	else:
		print('Wrong!')

testFunction(v)

print('hello word!')
print('what is your name')

myName = input()
print('It is good to meet you ', myName)
print('The length of your name is:', str(len(myName)))
#print(len(myName))
print('what is your age')
myAge = input()
print('you will be ' + str(int(myAge) + 1) + ' in a year')