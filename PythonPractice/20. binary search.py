'''Write a function that takes an ordered list of numbers (a list where the elements are
in order from smallest to largest) and another number. The function decides whether or not
 the given number is inside the list and returns (then prints) an appropriate boolean.
Extras:
Use binary search.'''

print(list((1, 2, 3, 4, 5, 6, 7, 8, 9)))
print(list(range(3)))

tl = list(input("enter a list: "))
num = str(input("enter a number: "))

'''if num in tl:
    print(True)
else:
    print(False)'''

mid = len(tl)//2
a = tl

if a[mid] == num:
    print('true')
else:
    while a[mid] != num and mid > 1:
        if a[mid] < num:
            a = [a[x] for x in a if int(x) > mid]
            mid = len(tl)//2
            print(a)
        elif a[mid] > num:
            a = [a[x] for x in a if int(x) < mid]
            mid = len(tl)//2
            print(a)
        else:
            print('false')

