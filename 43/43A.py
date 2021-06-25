n = int(input())
x = input()
y = ''
a=1
b=0
for i in range(n-1):
    team = input()
    if team == x:
        a +=1
    else:
        y=team
        b+=1
if (a>b):
    print(x)
else:
    print(y)