def counter(num):
    count=1
    while count <=num:
        yield count
        count+=1
count=counter(7)
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
