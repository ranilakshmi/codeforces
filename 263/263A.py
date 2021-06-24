i =0
while(True):
    i +=1
    a = [int(k) for k in input().split()]
    if (1 in a):
        break
j = a.index(1) + 1
print(abs(3 - i)+abs(3-j))