# -*- coding: utf-8 -*-
#%%구구단
a = int(input())
for i in range(1,10,1):
    b = a * i
    print("%.0f * %.0f = %.0f"%(a,i,b))

#%%2017
x,y = map(int,input().split())
sum = 0
for i in range(1,x,1):
    if i in [1,3,5,7,8,10,12]:        
        sum += 31
    elif i == 2:
        sum += 28
    else :
        sum += 30
        
for j in range(1,y+1,1):
    sum += 1
       
z = sum%7
h = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
for i in range (7):
    if i == z:
        print("%s"%h[i])
        
