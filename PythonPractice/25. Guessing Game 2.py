'''This time, we’re going to do exactly the opposite. You, the user, will have in your head
 a number between 0 and 100. The program will guess a number, and you, the user, will say
 whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get
your number'''

i = 0
g = 50
h = 100
l = 0
a = 1010101
loop = False

print("Is the number you're thinking of 50?")
while loop is False:
    answer = str(input())
    if answer == '=':
        print("It took me", i, "guesses." )
        break
    elif answer == ">":
        i += 1
        a = g
        g = (g+h)//2
        l = a
    elif answer == '<':
        i += 1
        a = g
        g = (g+l)//2
        h = a
    print("Is the number you're thinking of", g,"?")