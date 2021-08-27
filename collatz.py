#!/usr/bin/env python
#Collatz clac
import sys

def Collatz(number):
	if number % 2 == 0:
		temp = number // 2
	else:
		temp = number * 3 + 1

	print(str(temp))
	return temp

print('Please input a number:')

#inputNumber = int(input())
inputNumber = input()
try:
	inputNumber = int(inputNumber)
except ValueError:
	print('Please put an int number!')
sys.exit()

while inputNumber != 1:
	inputNumber = Collatz(inputNumber)


