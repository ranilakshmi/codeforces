n=int(input())
x=0
g=0
for i in range(0,n):
    a=int(input())
    if a!=x:
        g=g+1
    x=a
print(g)
