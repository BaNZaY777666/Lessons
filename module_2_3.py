my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = -1
while my_list[x] >= 0:
    x += 1
    if my_list[x] == 0:
        continue
    elif my_list[x] > 0:
        print(my_list[x])
    else:
        break