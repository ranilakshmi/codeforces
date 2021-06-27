binary = int(input())
i=0
decimal = 0
while binary>0:
    decimal = decimal + binary%10 * (2**i)
    i = i+1
    binary= binary//10
r =0
p=1
while p< decimal:
    p = p*4
    r = r+1
print(r)