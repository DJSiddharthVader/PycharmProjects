'''and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on
two lists of different sizes.'''

def common(a,b):
    blank = []
    if len(a) >= len(b):
        for x in a:
            for y in b:
                if x == y:
                    blank.append(x)
                else:
                    continue
    else:
        for x in b:
            for y in a:
                if y == x:
                    blank.append(y)
                    print(y)
                else:
                    continue
    print(blank)

x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common(x,y)