#!/usr/bin/python

def fibonacci(num):
	a,b=1,0
	for i in range(num):
		a,b=b,a+b
		if i!=(num-1):
			print(b, end=', ')
		else:
			print(b)
	return b

number=int(input("fibonacci number? "))

print("F%d = %d" %(number, fibonacci(number)))
