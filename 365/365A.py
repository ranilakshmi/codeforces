n,k = [int(i) for i in input().split()]
r = n
for i in range(n):
    s = input()
    for j in range(0,k+1):
        if str(j) not in s:
            r -=1
            break
print(r)