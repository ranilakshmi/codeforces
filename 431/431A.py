a = [int(i) for i in input().split()]
s = input()
r=0
for i in range(1,5):
    r = r + (s.count(str(i)) * a[i-1])
print(r)