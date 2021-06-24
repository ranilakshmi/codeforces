n = int(input())
crime = [int(i) for i in input().split()]
officer = 0
untreated_crime = 0
for i in range(n):
    if crime[i]==-1:
        if officer == 0:
            untreated_crime += 1
        else:
            officer -= 1
    else:
        officer = officer + crime[i]
print(untreated_crime)