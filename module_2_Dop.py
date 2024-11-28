import random

items = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
select_random = random.choice(items)
print(select_random)

count_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
password = []

for i in range(0,select_random):
    for j in range(1, select_random):
        sum = count_1[i] + count_1[j]
        if count_1[i] == count_1[j]:
            continue
        if count_1[i] > count_1[j]:
            continue
        if select_random % sum == 0 or sum == select_random:
            password.append(i+1)
            password.append(j+1)
        else:
            continue
print(*password, sep='')