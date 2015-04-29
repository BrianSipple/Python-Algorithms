def swap(item_list, swap_pos, with_pos):
    item_list[swap_pos], item_list[with_pos] = item_list[with_pos], item_list[swap_pos]



def selection_sort(item_list):

    if not isinstance(item_list, list):
        item_list = list(item_list)

    for i in range(len(item_list)):

        min_found = item_list[i]
        min_pos = None

        for j in range(i, len(item_list)):

            if item_list[j] < min_found:
                min_found = item_list[j]
                min_pos = j

        if min_pos is not None:
            swap(item_list, i, min_pos)

    return item_list


if __name__ == '__main__':

    print(selection_sort([435, 56, 735, 25875, 8234546, 78, 75, 245, 748245, 357]))
