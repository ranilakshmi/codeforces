n,m = [int(i) for i in input().split()]
color = ['C','M','Y']
r = True
for i in range(n):
    a = [k for k in input().split()]
    for j in range(3):
        if color[j] in a:
            r = False
if r == True:
    print("#Black&White")
else:
    print("#Color")