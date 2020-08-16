n=int(input())
q=input()
s=list(q)
x=(s.count('z'))
y=(s.count('n'))
for i in range(0,y):
    print("1",end=" ")
for j in range(0,x):
    print("0",end=" ")
