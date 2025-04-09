p = (4, 5)
x, y = p
x
# 4
y
# 5
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name
# 'ACME'
date
# (2012, 12, 21)
name, shares, price, (year, mon, day) = data
name
# 'ACME'
year
# 2012
mon
# 12
day
# 21
p = (4,5)
x, y, z = p
s = 'Hello'
a, b, c, d, e = s
a
# 'H'
b
# 'e'
e
# 'o'
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, prices, _ = data
shares
# 50
price
# 91.1
price
# 91.1
