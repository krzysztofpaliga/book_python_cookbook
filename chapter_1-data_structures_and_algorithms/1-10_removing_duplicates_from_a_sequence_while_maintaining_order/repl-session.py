def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


#
a = [1, 5, 2, 1, 9, 1, 5, 10]
#
list(dedupe(a))
#
# [1, 5, 2, 9, 10]
dedupe(a)
#
# <generator object dedupe at 0x7f0fbe0daea0>


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


#
#
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
#
#
list(dedupe(a, key=lambda d: (d['x'], d['y'])))
#
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
list(dedupe(a, key=lambda d: d['x']))
#
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
a
#
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
