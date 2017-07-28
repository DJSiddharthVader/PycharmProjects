'''Create a program that asks the user to enter their name and their age.
Print out a message addressed to
 them that tells them the year that they will turn 100 years old.'''

def hundoyrs(name,age):
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    hyr = 100 - age + 2016
    print(name, " will be one-hundred in the year ", hyr)
