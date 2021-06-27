n = int(input())
a =[int(i) for i in input().split()]
c = []
for i in range(n):
    c.append(a.count(a[i]))
r = "YES"
if n%2 == 0:
    if max(c) > n//2:
        r = "NO"
else:
    if max(c) > (n+1)//2:
        r = "NO"
print(r)