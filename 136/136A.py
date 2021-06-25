n = int(input())
present = [int(i) for i in input().split()]
for i in range(1,n+1):
    print(present.index(i) + 1,end = " ")