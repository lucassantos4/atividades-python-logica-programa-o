
vert = [1, 2, 5, 3, 6, 8, 7]

for i in range(0, 7):

    for j in range(i + 1, 7):

        if vert[i] > vert[j]:
            vert[i], vert[j] = vert[j], vert[i]

print(vert)
