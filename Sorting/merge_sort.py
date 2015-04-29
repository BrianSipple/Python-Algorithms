"""
Merge sort is a recursive algorithm that continually
splits a list in half. If the list is empty or has one item,
it is sorted by definition (the base case).

If the list has more than one item, we split the list and recursively
invoke a merge sort on both halves. Once the two halves are sorted,
the fundamental operation, called a merge, is performed.
"""
import math

def merge(L1, L2, L):
    """
    Merge 2 sorted lists, L1 and L2, into a properly-sized list, L
    """
    i = j = k = 0

    while k < len(L):

        if j == len(L2) or (i < len(L1) and L1[i] < L2[j]):
            L[k] = L1[i]
            i +=1
        else:
            L[k] = L2[j]
            j += 1

        k += 1


def merge_sort(L):

    if len(L) <= 1:  # Base case -- we're already sorted
        return L

    # DIVIDE (make copies of the halves)
    mid_pos = len(L) // 2
    L1 = L[:mid_pos]
    L2 = L[mid_pos:]

    # CONQUER (recursively stack up our sorts)
    merge_sort(L1)
    merge_sort(L2)

    # Merge the results after all recursions up to this point
    merge(L1, L2, L)

    return L






def bottom_up_merge(src, result, start, inc):
    """
    Merge src[start:start+inc] and src[start+inc:start+2 inc] into result.
    """

    end1 = start + inc                        # boundary for run 1
    end2 = min(start + 2 * inc, len(src))     # boundary for run 2

    x, y, z = start, start + inc, start       # index into run1, run2, result

    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1
        else:
            result[z] = src[y]
            y += 1

        z += 1

    if x < end1:
        result[z:end2] = src[x:end1]

    elif y < end2:
        result[z:end2] = src[y:end2]



def bottom_up_merge_sort(L):

    n = len(L)
    log_n = math.ceil(math.log(n, 2))

    source, dest = L, [None] * n

    for i in (2**k for k in range(log_n)):
        for j in range(0, n, 2*i):
            bottom_up_merge(source, dest, j, i)
        source, dest = dest, source


    if L is not source:
        L[:n] = source[:n]

    return L














if __name__ == '__main__':

    print(merge_sort([0, 345, 13345, 245435, 34, 46, 8, 567, 78, 3456, 249, 3]))
    print(bottom_up_merge_sort([0, 345, 13345, 245435, 34, 46, 8, 567, 78, 3456, 249, 3]))
