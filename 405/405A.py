n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
for i in range(n):
    print(a[i],end =" ")