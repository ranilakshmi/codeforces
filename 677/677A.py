n,h = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
max_width = 0
for i in range(len(a)):
    if a[i] > h :
        max_width += 1
max_width = max_width + n
print(max_width)