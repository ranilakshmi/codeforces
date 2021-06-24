n = int(input())
a = []
b = []
r = 0
for i in range(n):
    x,y = [int(j) for j in input().split()]
    a.append(x)
    b.append(y)
for i in range(n):
    r = r + b.count(a[i])
print(r)