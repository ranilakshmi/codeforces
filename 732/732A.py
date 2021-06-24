k,r = [int(i) for i in input().split()]
if k%10 == 0 or k==r or (k-r)%10 == 0:
    print(1)
else:
    i=2
    while (i<10):
        if (k*i%10 == 0) or ((k*i - r)%10 == 0):
            break
        i +=1
    print(i) 
