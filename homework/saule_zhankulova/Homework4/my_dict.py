my_dict = {'tuple': ('Monday', 1, 'Tuesday', 2, 'Wednesday', True),
           'list': ['January', 3, 'February', 4, 'March', 5],
           'dict': {'winter': 'December', 'spring': 'April', 'summer': 'June', 'autumn': 'September',
                    'noseason': False},
           'set': {True, 31, 'Friday', 'August', 'October'}
           }
print(my_dict['tuple'][-1])
my_dict['list'].append(True)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = True
my_dict['dict'].pop('winter')
my_dict['set'].add(69)
my_dict['set'].remove(31)
print(my_dict.items())
