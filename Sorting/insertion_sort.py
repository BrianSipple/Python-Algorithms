def swap(item_list, item_pos, with_pos):
    item_list[swap_pos], item_list[with_pos] = item_list[with_pos], item_list[swap_pos]


def insertion_sort(item_list):

    if not isinstance(item_list, list):
        item_list = list(item_list)

    for i in range(1, len(item_list)):

        j = i
        searching = True
        while j > 0 and searching:

            if item_list[j-1] > item_list[j]:
                swap(item_list, j-1, j)
                j -= 1

            else:
                searching = False

    return item_list


if __name__ == '__main__':

    print(insertion_sort('google'))
    print(insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
