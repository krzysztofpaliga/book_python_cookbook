from operator import itemgetter
rows = [
    #
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    #
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    #
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    #
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    #
]
#
#
rows_by_fname = sorted(rows, key=itemgetter('fname'))
#
rows_by_uid = sorted(row, key=itemgetter('uid'))
#
rows_by_uid = sorted(rows, key=itemgetter('uid'))
#
print(rows_by_fname)
#
# [{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]
print(rows_by_uid)
#
# [{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
#
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
#
print(rows_by_lfname)
#
# [{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
#
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
#
min(rows, key=itemgetter('uid'))
#
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
#
max(rows, key=itemgetter('uid'))
#
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
