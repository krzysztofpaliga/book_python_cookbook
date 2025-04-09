import heapq
#
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
#
print(heapq.nlargest(3, nums))
#
# [42, 37, 23]
print(heapq.nsmallest(3, nums))
#
# [-4, 1, 2]
portfolio = [
#
	{'name': 'IBM', 'shares': 100, 'price': 91.1},
#
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
#
{'name': 'FB', 'shares': 200, 'price': 21.09},
#
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
#
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
#
{'name': 'ACME', 'shares': 75, 'price': 115.65}
#
]
#
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
#
cheap
#
# [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
#
expensive
#
# [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]
heap = list(nums)
#
heapq.heapify(heap)
#
heap
#
# [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
heapq.heappop(heap)
#
# -4
heapq.heappop(heap)
#
# 1
heapq.heappop(heap)
#
# 2
