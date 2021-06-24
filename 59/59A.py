s = input()
l =0
for char in s:
    if char == char.lower():
        l +=1
if (len(s) - l > l):
    print(s.upper())
else:
    print(s.lower())