class User:
	def __init__(self, user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'User({})'.format(self._user_id)

#
users = [User(23), User(3), User(99)]
#
users
#
class User:
	def __init__(self, user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'User({})'.format(self.user_id)

#
users = [User(23), User(3), User(99)]
#
users
#
# [User(23), User(3), User(99)]
sorted(users, key=lambda u: u.user_id)
#
# [User(3), User(23), User(99)]
from operator import attrgetter
#
sorted(users, key=attrgetter('user_id'))
#
# [User(3), User(23), User(99)]
