n = int(input())
s = input()
r =0
for i in range(1,len(s)):
    if s[i-1] == s[i]:
        r +=1
print(r)