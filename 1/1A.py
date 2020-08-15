n,m,a=[int(i)for i in input().split()]
if n%a==0:
    p=n//a
else:
    p=(n//a)+1
if m%a==0:
    q=m//a
else:
    q=(m//a)+1
x=p*q
print(x)
