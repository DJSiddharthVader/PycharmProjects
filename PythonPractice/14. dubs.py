'''Write a program (function!) that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list,
and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a
different function.'''

def dups(z):
    return(print(set(z)))

def dups2(z):
    b = []
    for x in z:
        for y in z:
            if x != y:
                b.append(x)
    return(print(z))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

dups(a)

dups2(a)