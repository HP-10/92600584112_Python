user_name = input("Enter User Name: ")
user_pass = input("Enter Password: ")

# Demonstration of if-else statement
if user_pass == "1234":
    print("\nLogin Successful...")

    print("\nEnter marks between 0 and 100")

    sub1 = int(input("Enter Python marks: "))
    sub2 = int(input("Enter AI/ML marks: "))
    sub3 = int(input("Enter DBMS marks: "))
    sub4 = int(input("Enter OS marks: "))

    # Demonstration of if statement
    if (sub1 >= 0 and sub1 <= 100 and
        sub2 >= 0 and sub2 <= 100 and
        sub3 >= 0 and sub3 <= 100 and
        sub4 >= 0 and sub4 <= 100):

        total_marks = sub1 + sub2 + sub3 + sub4
        percentage = (total_marks / 400) * 100

        print("\nTotal Marks:", total_marks)
        print("Percentage:", percentage, "%")

        # Demonstration of if-elif-else statement
        if percentage < 35:
            print(user_name, "failed in the examination.")
        elif percentage <= 50:
            print(user_name, "got 'D Grade' in the examination.")
        elif percentage <= 70:
            print(user_name, "got 'C Grade' in the examination.")
        elif percentage <= 80:
            print(user_name, "got 'B Grade' in the examination.")
        elif percentage <= 90:
            print(user_name, "got 'A Grade' in the examination.")
        elif percentage <= 100:
            print(user_name, "got 'A+ Grade' in the examination.")
        else:
            print("Invalid Percentage.")

    else:
        print("\nInvalid marks! Please enter marks between 0 and 100.")

else:
    print("\nInvalid Password.")
