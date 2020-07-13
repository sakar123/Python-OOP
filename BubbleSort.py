"""Python program to demonstrate bubble sorting
a) Bubble Sort   The time complexity for this sorting is O(n^2)"""


def bubble_sort(given_list):
    a = 0
    for i in given_list:
        for j in range(len(given_list)-1):
            if given_list[j] > given_list[j+1]:
                swap = given_list[j+1]
                given_list[j+1] = given_list[j]
                given_list[j] = swap
                a += 1

                print(given_list)
    print(a)
    return given_list


print("Final SOrted Form: ", bubble_sort([6, 4, 3, 9, 12, 46, 1, 2]))





