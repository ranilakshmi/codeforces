n = input()
a=[]
for i in n:
    a.append(int(i))
r=''
if a[0] != 9:
    a[0] = min(a[0],9-a[0])
    r= r +str(a[0])
else:
    r=str(a[0])
for i in range(1,len(a)):
    a[i] = min(a[i],9-a[i])
    r = r+str(a[i])
print(r)