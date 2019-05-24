
number = 600_851_475_143
prime_list = list()

while number > 1000:
    for val in range(3, 10000, 2):
        if number % val == 0:
            break
    number = number / val
    prime_list.append(val)
print(prime_list)
