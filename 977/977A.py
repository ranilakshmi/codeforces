n,k=[int(i) for i in input().split()]
if n<(10**9)+1 and n>1 and k<51 and k>0:
    for x in range(1,k+1):
        if n%10==0:
            n=n//10
        else:
            n=n-1
print(n)
