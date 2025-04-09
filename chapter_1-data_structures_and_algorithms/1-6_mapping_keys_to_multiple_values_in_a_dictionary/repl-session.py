d = {
#
	'a': [1, 2, 3],
#
	'b': [4, 5]
#
}
#
d
#
# {'a': [1, 2, 3], 'b': [4, 5]}
d
#
# {'a': [1, 2, 3], 'b': [4, 5]}
e = {
#
	'a': {1, 2, 3},
#
	'b': {4, 5}
#
}
#
from collections import defaultdict
#
d = defaultdict(list)
#
d['a'].append(1)
#
d['a'].append(2)
#
d['b'].append(4)
#
d
#
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})
d = {}
#
d.setdefault('a', []).append(1)
#
d
#
# {'a': [1]}
d.setdefault('a', []).append(2)
#
d
#
# {'a': [1, 2]}
d.setdefault('b', []).append(4)
#
d
#
# {'a': [1, 2], 'b': [4]}
d = {}
#
