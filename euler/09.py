
triplets = []
for i in range(1, 1000):
    for j in range(1, 1000):
        total = i**2 + j**2
        if (total ** (1/2)).is_integer():
            triplets.append((i, j, total ** (1/2)))

for triplet in triplets:
    if sum(triplet) == 1000:
        print(triplet)

print(200 * 375 * 425)