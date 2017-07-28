'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
guess the number, then tell them whether they guessed too low, too high, or exactly
right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken,
and when the game ends, print this out.'''


from random import randint

num = randint(1,9)

g = 10
n = 0
while g != num:
    g = int(input("guess a number: "))
    if g > num:
        print('too high')
        n += 1

    if g < num:
        print('too low')
        n +=1

print('right', n)

