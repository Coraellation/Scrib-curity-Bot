__author__ = 'George'

trans = 1.25

c = [16.35, 0,0,0,0,0,0,0,0]
for i in range(1, 9):
    c[i] = 2*c[i-1]

d = [18.35, 0,0,0,0,0,0,0,0]
for i in range(1, 9):
    d[i] = 2*d[i-1]

e = [20.6, 0,0,0,0,0,0,0,0]
for i in range(1, 9):
    e[i] = 2*e[i-1]

f = [21.38, 0,0,0,0,0,0,0,0]
for i in range(1, 9):
    f[i] = 2*f[i-1]

g = [24.5, 0,0,0,0,0,0,0,0]
for i in range(1, 9):
    g[i] = 2*g[i-1]

a = [27.5, 0,0,0,0,0,0,0,0]
for i in range(1, 9):
    a[i] = 2*a[i-1]

b = [30.87, 0,0,0,0,0,0,0,0]
for i in range(1, 9):
    b[i] = 2*b[i-1]

for i in range(1, 9):
    c[i]*=trans
    d[i]*=trans
    e[i]*=trans
    f[i]*=trans
    g[i]*=trans
    a[i]*=trans
    b[i]*=trans