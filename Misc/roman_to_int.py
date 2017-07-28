chars = ("M", "D", "C", "L", "X", "V", "I")
vals = (1000, 500, 100, 50, 10, 5, 1)


def lookup(c):
    """
    returns the roman numeral value corresponding to the character c
    :param c: roman numeral
    :return: value
    """
    if c not in chars:
        return ValueError
    p = chars.index(c)
    return vals[p]


def romantoint(r):
    t = 0
    for x in r:
        v = lookup(x)
        z = r.index(x)
        if lookup(x) < lookup(x + 1):
            t -= v
        elif x == len(r):
            t += v
        else:
            t += v
    return t
