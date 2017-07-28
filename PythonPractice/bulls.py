'''
Randomly generate a 4-digit number.
Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.” Every time the
user makes a guess, tell them how many “cows” and “bulls” they have. Once the user
guesses the correct number, the game is over. Keep track of the number of guesses
the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look
like this:

  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.'''

import random as rd

q = rd.randrange(9)
w,e,r = 10, 10, 10
while w > 9 or w == q:
    w = rd.randrange(9)
while e > 9 or e == q or e == w:
    e = rd.randrange(9)
while r > 9 or r == q or r == w or r == e:
    r = rd.randrange(9)

num = str(q) + str(w) +str(e) + str(r)
print(num)

cow = 0
bull = 0
i = 1

guess = str(input("Guess a number:"))

while guess != num:
    i += 1
    for y in guess:
        if y in num:
            if num.index(y) != guess.index(y):
                bull += 1
    x = 0
    while x < 4:
        if num[x] == guess[x]:
            cow += 1
        x += 1
    print('bull:', bull, '\n', 'cow:', cow)
    cow = 0
    bull = 0
    guess = str(input("Guess again:"))
else:
    print(i, '\n', "you win!")










