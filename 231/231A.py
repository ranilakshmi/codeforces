n = int(input())
result =0
for i in range(n):
    a,b,c = [int(j) for j in input().split()]
    if a+b+c > 1:
        result +=1
print(result)