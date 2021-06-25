n,x = [int(i) for i in input().split()]
kid =0
for i in range(n):
    a,b =[i for i in input().split()]
    b = int(b)
    if a=='+':
        x = x + b
    else:
        if x>=b:
            x -= b
        else:
            kid += 1
print(x,kid)