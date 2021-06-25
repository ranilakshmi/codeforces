s = input()
distinct = set()
for char in s:
    if char.isalpha():
        distinct.add(char)
print(len(distinct))