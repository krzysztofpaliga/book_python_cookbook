def drop_first_last(grades):
	first, *middle, last = grades
	return sum(middle)/len(middle)

#
drop_first_last([1,2,3,4,5,6,7,8,9])
#
# 5.0
record = ('Dave', 'dave@example.com', '773-123', '234-234', '234-123')
#
name, email, *phone_numbers = record
#
name
#
# 'Dave'
email
#
# 'dave@example.com'
phone_numbers
#
# ['773-123', '234-234', '234-123']
sales_record = [1234, 4567, 8901]
#
*trailing_qtrs, current_qtr = sales_record
#
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
#
trailing_avg
#
# 2900.5
records = [
#
	('foo', 1, 2),
#
	('bar', 'hello'),
#
	('foo', 3, 4),
#
]
#
def do_foo(x, y):
	print('foo', x, y)

#
def do_bar(s):
	print('bar', s)

#
for tag, *args in records:
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)

#
# foo 1 2
# bar hello
# foo 3 4
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
#
uname, *fields, homedir, sh = line.split(':')
#
uname
#
# 'nobody'
homedir
#
# '/var/empty'
sh
#
# '/usr/bin/false'
record = ('ACME', 50, 123.45, (12, 18, 2012))
#
name, *_, (*_, year) = record
#
name
#
# 'ACME'
year
#
# 2012
items = [1, 10, 7, 4, 5, 9]
#
head, *tail = items
#
head
#
# 1
tail
#
# [10, 7, 4, 5, 9]
def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else head

#
sum(items)
#
# 36
