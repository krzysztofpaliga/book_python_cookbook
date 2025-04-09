prices = {
#
	'ACME': 45.23,
#
	'AAPL': 612.78,
#
	'IBM': 205.55,
#
	'HPQ': 37.20,
#
	'FB': 10.75
#
}
#
#
min_price = min(zip(prices.values(), prices.keys()))
#
min_price
#
# (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
#
max_price
#
# (612.78, 'AAPL')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
#
prices_sorted
#
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]
min(prices)
#
# 'AAPL'
max(prices)
#
# 'IBM'
min(prices.values())
#
# 10.75
max(prices.values())
#
# 612.78
min(prices, key=lambda k:prices[k])
#
# 'FB'
max(prices, key=lambda k:prices[k])
#
# 'AAPL'
min_value = prices[min(prices, key=lambda k:prices[k])
#
min_value
#
min_value = prices[min(prices, key=lambda k:prices[k])]
#
min_value
#
# 10.75
prices = { 'AAA': 45.23, 'ZZZ': 45.23 }
#
min(prices, key=lambda k:prices[k])
#
# 'AAA'
min(zip(prices.values(), prices.keys()))
#
# (45.23, 'AAA')
max(zip(prices.values(), prices.keys()))
#
# (45.23, 'ZZZ')
