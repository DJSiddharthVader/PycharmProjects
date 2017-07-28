'''Ask the user for a number. Depending on whether the number is even or odd, print out
an appropriate message to the user. Hint: how does an even / odd number react differently
 when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number
 to divide by (check). If check divides evenly into num, tell that to the user.
 If not, print a different appropriate message.'''

def oddoreven(x,y)
    x = int(input("Enter a number: "))
    y = int(input("Enter a second number: "))
    if y != 0:
        if x%y == 0:
            print("does divide evenly")
        else:
            print("doesn't divide evenly")
    else:
        if x%2 == 0:
            if x%4 == 0:
                print("divisible by 4")
            else:
                print("Even")
        else:
            print("Odd")


