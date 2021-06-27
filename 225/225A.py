n = int(input())
t = int(input())
x = [1,2,3,4,5,6]
a,b = [int(j) for j in input().split()]
side = [a,b,7-a,7-b]
top = [t,7-t]
r ="YES"
for i in range(n-1):
    a,b = [int(j) for j in input().split()]
    side = [a,b,7-a,7-b]
    if (top[0] in side or top[1] in side):
        r = "NO"
        break
    top =[]
    for j in range(1,7):
        if j not in side:
            top.append(j)
print(r)