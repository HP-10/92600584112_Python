numbers = [10, 13, 17, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Numbers after applying break, continue and pass:")

for num in numbers:

    # continue skips even numbers
    if num % 2 == 0:
        continue

    # pass does nothing when num is 30
    if num == 30:
        pass

    # break terminates the loop when num is 80
    if num == 80:
        break

    print(num)
