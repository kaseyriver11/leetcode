
total = 0
current_one = 0
current_two = 1

while current_two < 4_000_000:
    new = current_one + current_two
    current_one = current_two
    current_two = new

    if current_two % 2 == 0:
        total += current_two

print(total)
