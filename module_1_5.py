tuple_1 = (1, 2, 'a', 'b')
# tuple_1 [0] = 2 # картеж не может быть изменен. Могут быть измененны только данные в нем, если они записаны в виде списка
immutable_var = (tuple_1)
print('Immutable tuple:', (immutable_var))

tuple_2 = [1, 0, 'a', 'b'], ['Modified']
mutatble_list = (tuple_2)
tuple_2 [0][1] = tuple_2[0][0] + tuple_2[0][1]+1
print('Mutable list:', (mutatble_list))