"""
The shell sort, sometimes called the “diminishing increment sort,”
improves on the insertion sort by breaking the original
list into a number of smaller sublists, each of which
is sorted using an insertion sort. The unique way that
these sublists are chosen is the key to the shell sort.

Instead of breaking the list into sublists of contiguous items,
the shell sort uses an increment i, sometimes called the gap,
to create a sublist by choosing all items that are i items apart.
"""

def swap(item_list, swap_pos, with_pos):
    item_list[swap_pos], item_list[with_pos] = item_list[with_pos], item_list[swap_pos]



def shell_sort(item_list):

    if not isinstance(item_list, list):
        item_list = list(item_list)

    num_sublists = len(item_list) // 2

    while num_sublists > 0:

        for i in range(num_sublists):
            gap_insertion_sort(item_list, i, num_sublists)

        print(
            "After increments of size {}, the list is {}"
                .format(num_sublists, item_list)
        )

        num_sublists //= 2


def gap_insertion_sort(item_list, start_pos, gap_size):

    for i in range(start_pos + gap_size, len(item_list), gap_size):

        searching = True
        j = i

        while searching and j > start_pos:

            if item_list[j-gap_size] > item_list[j]:
                swap(item_list, j-gap_size, j)
                j -= gap_size

            else:
                searching = False




if __name__ == '__main__':

    print(shell_sort([0, 345, 13345, 245435, 34, 46, 8, 567, 78, 3456, 249, 3]))
