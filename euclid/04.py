
best = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        number = i * j
        str_number = str(number)
        if len(str_number) % 2 == 0:
            mid = len(str_number) / 2
            front = str_number[0:int(mid)]
            back = str_number[int(mid):][::-1]
            if front == back:
                if number > best:
                    best = number
        else:
            continue
