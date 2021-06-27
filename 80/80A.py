def is_prime(n):
    for i in range(2,n//2 + 1):
        if n%i == 0:
            return False
    return True
r = "YES"
n,m = [int(i) for i in input().split()]
for i in range(n+1,m):
    if is_prime(i) == True:
        r = "NO"
        break
if is_prime(m) == False:
    r = "NO"
print(r)