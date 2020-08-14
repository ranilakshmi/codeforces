n=int(input())
if n%2==0:
    x=n//2
    print(x)
    for i in range(0,x):
        print(2,end=" ")
if n%2==1:
    x=n//2-1
    print(x+1)
    for i in range(0,x):
        print(2,end=" ")
    print(3)
