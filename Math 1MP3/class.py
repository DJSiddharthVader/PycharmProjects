import numpy as np
a = np.arange(1,8)
b = a**2
c = b.mean()
print(c.mean())


x = np.arange(0, 1, 0.2)
z = (x,x,x,x,x)
y = np.reshape(z, (5,5))
print(y)

d = np.arange(9)
e = d.reshape(3,3)
print(e)

aa = np.array((x,)*5)
print(aa)

q = np.arange(21).reshape(3,7)
w = q.reshape(7,3)
s = np.dot(q,w)
print(s)
