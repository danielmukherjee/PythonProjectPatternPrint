def pattern():
    try:
        a = int(input("Enter any Intiger number: "))
        b = int(input("Either 0 or 1 : "))
        if b == 0:
            x = 0
            while (x <= a):
                print("*" * x, end="\n")
                x = x + 1

        elif b == 1:
            x = a
            while (x != 0):
                print("*" * x, end="\n")
                x = x - 1

        else:
            print("Not Valid, Please Try Again")

    except Exception as e:
        print(e, "Invalid Input, Please Try Again")

    again()

def again():
    try:
        ag = input("Do you want to print again?\n Press y for Yes and n for No:\n")
        if ag == "y" or ag == "Y":
            pattern()
        elif ag == "n" or ag == "N":
            print("Bye... Have a Nice Day!!")
        else:
            print("Invalid Input")
            again()

    except Exception as e:
        print(e, "Invalid Input, Please Try Again")

pattern()

