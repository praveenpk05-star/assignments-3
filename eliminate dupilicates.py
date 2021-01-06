ints_list = [1, 2, 3, 4, 3, 2 ,5,8,9,5]

temp = []

for x in ints_list:
    if x not in temp:
        temp.append(x)

ints_list = temp

print('Updated List after removing duplicates =', temp )