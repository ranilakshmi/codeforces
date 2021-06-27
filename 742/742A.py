n = int(input())
r = n%4
if n==0:
    print(1)
elif (r==1):
    print(8)
elif (r==2):
    print(4)
elif (r==3):
    print(2)
else:
    print(6)