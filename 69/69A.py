n=int(input())
a=0
b=0
c=0
for i in range(n):
    x,y,z=[int(i) for i in input().split()]
    a=a+x
    b=b+y
    c=c+z
if a==0 and b==0 and c==0:
    print("YES")
else:
    print("NO")
