num = int(input("Enter any number: "))

digit_sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

print("Sum of digits of", num, "=", digit_sum)
