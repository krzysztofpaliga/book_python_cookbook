a = {
#
	'x': 1,
#
	'y': 2,
#
	'z': 3
#
}
#
b = {
#
	'w': 10,
#
	'x': 11,
#
	'y': 2
#
}
#
a.keys() & b.keys()
#
# {'x', 'y'}
a.keys() - b.keys()
#
# {'z'}
a.items() & b.items()
#
# {('y', 2)}
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
#
c
#
# {'x': 1, 'y': 2}
