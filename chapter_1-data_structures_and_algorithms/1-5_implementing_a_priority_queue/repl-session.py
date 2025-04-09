import heapq
#


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

#


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


#
q = PriorityQueue()
#
q.push(Item('foo'), 1)
#
q
#
# <__main__.PriorityQueue object at 0x7f00079be590>
q.pop()
#
# Item('foo')
q
#
#
q.push(Item('foo'), 1)
#
q.pop()
#
# Item('foo')
q.push(Item('foo'), 1)
#
q.push(Item('bar'), 5)
#
q.push(Item('spam'), 4)
#
q.push(Item('grok'), 1)
#
q.pop()
#
# Item('bar')
q.pop()
#
# Item('spam')
q.pop()
#
# Item('foo')
q.pop()
#
# Item('grok')
q
#
# <__main__.PriorityQueue object at 0x7ff939dde290>
q._queue
#
# []
q.push(Item('foo', 1))
#
q.push(Item('foo'), 1)
#
q.push(Item('fooo'), 2)
#
q.push(Item('foooo'), 3)
#
q.push(Item('foooor'), 1)
#
q._queue
#
# [(-3, 8, Item('foooo')), (-1, 6, Item('foo')), (-2, 7, Item('fooo')), (-1, 9, Item('foooor'))]
a = Item('foo')
#
b = Item('bar')
#
a < b
#
#
a = (1, Item('foo'))
#
a = (2, Item('bar'))
#
a = (1, Item('foo'))
#
b = (2, Item('bar'))
#
a < b
#
# True
c = (1, Item('grok'))
#
a < c
#
a = (1, 0, Item('foo'))
#
b = (2, 1, Item('bar'))
#
c = (1, 2, Item('grok'))
#
a < b
#
# True
a < c
#
# True
