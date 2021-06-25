n = int(input())
children = [int(i) for i in input().split()]
a=[]
b=[]
c=[]
for i in range(n):
    if children[i] == 1:
        a.append(i+1)
    elif children[i] == 2:
        b.append(i+1)
    else:
        c.append(i+1)
teams = min(len(a),len(b),len(c))
print(teams)
for i in range(teams):
    print(a[i],b[i],c[i])