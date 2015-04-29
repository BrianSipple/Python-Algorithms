

def swap(item_list, swap_pos, with_pos):
    item_list[swap_pos], item_list[with_pos] = item_list[with_pos], item_list[swap_pos]


def quick_sort(L, start_pos=None, end_pos=None):
    """
    In-place version of quick sort using Python lists
    """

    if start_pos is None:
        start_pos = 0

    if end_pos is None:
        end_pos = len(L) - 1

    if end_pos < start_pos:
        # range is already sorted here
        return


    pivot_pos = end_pos  # Initialize the pivot_pos  # TODO: IMPLEMENT MEDIAN OF THREE APPROACH
    pivot_item = L[pivot_pos]

    # Initialize left and right markers, exclusive of the pivot_pos
    left_marker_pos = start_pos
    right_marker_pos = end_pos - 1

    # Calibrate our markers
    while True:

        # Stop left marker on the first value
        # in the list greater than the pivot val
        while left_marker_pos <= right_marker_pos \
            and L[left_marker_pos] <= pivot_item:

            left_marker_pos += 1

        # Stop the right marker on the first value in the
        # list less than the pivot value
        while right_marker_pos >= left_marker_pos \
            and L[right_marker_pos] >= pivot_item:

            right_marker_pos -= 1

        # Here, we've either crossed markers, or both have stopped
        # on an item that belongs on the other side
        # of the pivot position
        if right_marker_pos < left_marker_pos:
            break

        else:
            swap(L, left_marker_pos, right_marker_pos)

    # When the right marker position becomes less than
    # the left marker position, swap the pivot value
    # with the value in the left_marker position. THIS POSITION IS NOW SORTED
    swap(L, pivot_pos, left_marker_pos)

    # Recurse on the two new halves that we're designating,
    # taking care to do so around the positions that we've already sorted

    quick_sort(L, start_pos=start_pos, end_pos=left_marker_pos - 1)
    quick_sort(L, start_pos=left_marker_pos + 1, end_pos=pivot_pos)

    return L




if __name__ == '__main__':
    print(quick_sort([0, 345, 13345, 245435, 34, 46, 8, 567, 78, 3456, 249, 3]))
