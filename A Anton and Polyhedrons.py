n = int(input())
x = 0
for i in range(0,n):
    y = input()
    if y == "Tetrahedron":
        x+=4
    elif y == "Cube":
        x+=6
    elif y == "Octahedron":
        x+=8
    elif y == "Dodecahedron":
        x+=12 
    else:
        x+=20
print(x)