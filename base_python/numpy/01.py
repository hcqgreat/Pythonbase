import numpy as np

a = np.array([1, 2, 3])
print(a)
b = np.array([1, 2, 3], dtype=float, ndmin=3)
print(b)

c = np.arange(11)
print(c)
d = np.arange(1, 12, 3)
print(d)
e = np.arange(10, 20, 2, dtype=float)
print(e)

f = np.random.random(size=5)
print(f, type(f))

g = np.random.random(size=(3, 4))
print(g, type(g))

h = np.random.random(size=(2, 3, 4))
print(h)

i = np.zeros(5)
print(i)

