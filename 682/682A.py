n,m= [int(i) for i in input().split()]
a =[]
b =[]
pair =0
for i in range(4):
    a.append(n//5)
    b.append(m//5)
for i in range((n%5)):
    a[i] += 1
for i in range((m%5)):
    b[i] += 1
for i in range(4):
    pair += a[i]*b[3-i]
pair += (n//5)*(m//5)
print(pair)