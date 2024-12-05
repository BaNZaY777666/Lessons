calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    a = len(string)
    stringU = string.upper()
    stringL = string.lower()
    string_tuple = (a, stringU, stringL)
    return string_tuple


def is_contains(string, list_to_search):
    count_calls()
    string.lower()
    list_to_search = [i.lower() for i in list_to_search]
    if string.lower() in list_to_search:
        return True
    else:
        return False



print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)