try:
    a= int(input("Enter 1st number:"))
    b= int(input("Enter 2nd number:"))
    result=a/b

except ZeroDivisionError:
    print("Error: Number can not divisible by zero.")

except ValueError:
    print("Error: Please enter valid integers.")

else:
    print("Result =",result)
    print("No exception occurred.")

finally:
    print("Finally block is executed.")