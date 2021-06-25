n = int(input())
s = [int(i) for i in input().split()]
a = s.count(max(s))
b = s.count(min(s))
if min(s) != max(s):
    print(len(s) - (a+b))
else:
    print(0)