def meanderingArray(list):
    array = []
    for i in range(len(list)):
        list[i] = int(list[i])

    list.sort()
    print(list)
    tam = len(list)

    while tam > 0:
        array.append(max(list))
        list.remove(max(list))
        if (len(list) > 0):
            array.append(min(list))
            list.remove(min(list))
        tam = len(list)

    return array

n_str = input()
n = int(n_str)
i = 0
unsorted_list = []
while (i < n):
    unsorted_entry = input()
    unsorted_list.append(unsorted_entry)
    i = i + 1

res = meanderingArray(unsorted_list)
print(res)
