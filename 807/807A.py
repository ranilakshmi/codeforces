n = int(input())
l1 = []
l2 = []
for i in range(n):
    a,b = [int(j) for j in input().split()]
    l1.append(a)
    l2.append(b)
if (l1!=l2):
    print("rated")
else:
    l2.sort()
    l2.reverse()
    if l1 == l2:
        print("maybe")
    else:
        print("unrated")