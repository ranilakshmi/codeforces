a,b=[int(i) for i in input().split()]
if a>0 and b>=a and b<11:
    x=0
    while a<=b:
        a=a*3
        b=b*2
        x=x+1
    print(x)
