#!/usr/bin/python

myList=[]

number=int(input("how many numbers? "))
sum=0

for i in range(number):
	myList.append(int(input("input number(%d): " %(i+1))))
	sum+=myList[i]

average=sum/number
print(average)
