# -*- coding: utf-8 -*-

#%% A+B

a = input()
b = a.split(" ")
sum = 0
for i in b:
    sum += int(i)

print(sum)
#%% A-B
a = input()
b = a.split(" ")
sub =int(b[0]) - int(b[1])
print(sub)
#%% A+B-3
count = int(input())
a = input()
b = input()
c = input()
d = input()
e = input()
a1 = a.split(" ")
b1 = b.split(" ")
c1 = c.split(" ")
d1 = d.split(" ")
e1 = e.split(" ")
f= a1+b1+c1+d1+e1
for i in range(0,len(f),2):
    print(int(f[i])+int(f[i+1]))
#%% A+B-3
t = int(input())
f=[]
for i in range(t):
    a = input()
    t_s = a.split(" ")
    f += t_s

for y in range(0,len(f),2):
    print(int(f[y])+int(f[y+1]))
    
#%% A+B-3
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print(a+b)

#%% A+B-2
a=int(input())
b=int(input())
print(a+b)

#%% A+B-4
for i in range(5):
    a,b = map(int,input().split())
    print(a+b)
#%% A+B-4
while True:
    a,b = map(int,input().split())
    print(a+b)
    if b>10 :
        break

#%% A+B-4
try:
    while True:
        a,b = map(int,input().split())
        print(a+b)
except EOFError:
    quit()
#%% A+B-5
    


    