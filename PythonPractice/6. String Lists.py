'''Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)'''


z = str(input("please enter a word: "))
c = len(z)//2
for x in range(c):
    if z[x] == z[-(x+1)]:
        continue
    else:
        print("not pallindrome")
        raise ValueError
print("is pallindrome")
