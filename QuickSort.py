def partition(list, start, end):
    to_compare = list[end]
    p_index = start
    for i in range(start, end):
        if list[i] <= to_compare:
            swap = list[p_index]
            list[p_index] = list[i]
            list[i] = swap
            p_index += 1
    swap = list[p_index]
    list[p_index] = list[end]
    list[end] = swap
    return p_index


def QuickSort(list, start, end):
    if start < end:
        start_index = partition(list, start, end)
        QuickSort(list, start, start_index-1)
        QuickSort(list,start_index+1, end)

a_list = [5, 9, 1, 4, 8, 6]
QuickSort(a_list, 0, 5)
print(a_list)