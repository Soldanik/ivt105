# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 13:17:32 2018

@author: kiril
"""

#1 задание
a=[]
for i in range(900,799,-100):
    a.append(i)
print(a)

b=[]
for i in range(700,599,-100):
    b.append(i)
print(b)

c=[]
for i in range(500,399,-100):
    c.append(i)
print(c)

d=[]
for i in range(300,199,-100):
    d.append(i)
print(d)

s=[a,b,c,d]
print(s)

#2 задание 
a=[]
for i in range(1,4,1):
    a.append(i)
print(a)
b=[]
for i in range(4,7,1):
    b.append(i)
print(b)
c=[]
for i in range(7,10,1):
    c.append(i)
print(c)
s=[a,b,c]
print(s)

#3 задание
s=[]
for i in range (10,100,1):
    s.append(i)
    x=i//10
    y=i%10
    if y==8*x:
        print(i)
        
#4 задание
s = []
n = int(input())
for i in range(100, 1000, 1):
    s.append(i)
    x = i//100
    y = i%100//10
    z = i % 10
    if x+y+z==n:
        print(i)
        
#5 задание
num1 = int(input()) 
num2 = int(input()) 

for x in range(num1, num2 + 1): 
    if str(x) == str(x)[::-1] and len(str(x)) == 4:
        print(x)

#6 задание
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)

