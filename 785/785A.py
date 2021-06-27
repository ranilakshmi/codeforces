n = int(input())
side =0
for i in range(n):
    s = input()
    if s == "Tetrahedron":
        side += 4
    elif s =="Cube":
        side += 6
    elif s=="Octahedron":
        side += 8
    elif s == "Dodecahedron":
        side += 12
    else:
        side +=20
print(side)