'''Create a program that asks the user for a number and then prints out a list of all
the divisors of that number'''


a = list(range(10))
print(a)


x = int(input("number: "))
nums = list(range(x))
nums.pop(0)
divs = []
for y in nums:
    if x%y == 0:
        divs.append(y)
print(divs)