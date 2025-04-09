from collections import deque
#


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


#
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'wlp3s0', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*2)

#
q = deque(maxlen=3)
#
q.append(1)
#
q.append(2)
#
q.append(3)
#
q
#
# deque([1, 2, 3], maxlen=3)
q.append(4)
#
q
#
# deque([2, 3, 4], maxlen=3)
q.append(5)
#
q
#
# deque([3, 4, 5], maxlen=3)
q = deque()
#
q.append(1)
#
q.append(2)
#
q.append(3)
#
q.appendleft(3)
#
q
#
# deque([3, 1, 2, 3])
q.pop()
#
# 3
q
#
# deque([3, 1, 2])
q.popleft()
#
# 3
