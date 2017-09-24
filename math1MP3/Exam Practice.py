import numpy as np
'''
print(np.zeros(10))

x = np.zeros(10)
x[4] = 1
print(x)

print(np.arange(10,50))

def letter_count(str):
    d = {}
    STR = str.upper()
    for x in STR:
        if x in d.keys():
            d[x] += 1
        else:
            d[x] = 1
    return d

print(letter_count("Squeamish ossifrage"))


def make_change(amount, coin_values):
    change = []
    while amount > 0:
        for x in coin_values:
            y = 0
            while amount >= x:
                amount = amount - x
                y += 1
            change.append(y)
    return change

print(make_change(73,(25,10,5,1)))

def luckysum(val):
    sum = 0
    for x in val:
        if x == 13:
            break
        else:
            sum += x
    return sum

print(luckysum((1,2,3,13,2,5)))

def fun(v,d,t,m):
    it = 0
    while v >= t:
        v /= d
        it += 1
        if it >= m:
            raise ValueError
    print(it)
    return it

fun(1e9, 10, 11, 10)



list = [1,2,3]
list2 = [4,5]
list += list2
print(list)

print(5.72//2)'''

p = 10
r = 5
d = 2

print(p*r*d/100)

print((p*r*d)/100)

print(p/100*r*d)

y = np.array((2,2))
print(y)

t = 0

for x in range(2):
    t += y[x][x]
print(t)