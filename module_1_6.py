my_dict = {'Toma': 19, 'Roma': 22,'Katya': 6}
print('Dict:',my_dict)

print('Existing value:',my_dict['Toma'])
print('Not existing value:', my_dict.get('Boris'))

my_dict.update({'Slava': 59,
                'Vitya': 18})
Del_Val = 'Roma'
del my_dict[Del_Val]
print('Deleted value:', Del_Val)
print('Modefied dictionary:', my_dict)
print(' ')

my_set = {3,2,1,4,4,3,2,2,3,1,4,5, 'string', True,}
my_set.add('Apple')
my_set.add(12)
print('Set:', my_set)
my_set.remove(4)
print('Modefied set:', my_set)