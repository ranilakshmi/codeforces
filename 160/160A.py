n = int(input())
coin = [int(i) for i in input().split()]
coin.sort()
coin.reverse()
s = sum(coin)
r =0
i=0
while(r<=s-r):
    r = r+coin[i]
    i+=1
print(i)