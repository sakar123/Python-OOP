"""This is python program which demonsrates insertion sort"""

# [1, 2, 19, 4, 6, 0]


def insertion_sort(given_list):
    for i in range(1, len(given_list)):
        index = 0
        while index < i:
            if given_list[i] < given_list[index]:
                swap = given_list[i]
                given_list[i] = given_list[index]
                given_list[index] = swap
            index = index + 1

    return given_list


print("The sorted list: ", insertion_sort([4, 6, 3, 9, 12, 46, 1, 2]))

""""""
