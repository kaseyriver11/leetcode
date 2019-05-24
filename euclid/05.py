
new_product = 2 * 7 * 11 * 13 * 17 * 19 * 18 * 20

p = new_product
while p > 1_000_000:
    p = p - 20
    for i in range(20, 10, -1):
        if p % i != 0:
            break
    print(p)


p =  2 * 7 * 11 * 13 * 17 * 19 * 18 * 20

for i in range(20, 1, -1):
    if p % i != 0:
        print(i)

