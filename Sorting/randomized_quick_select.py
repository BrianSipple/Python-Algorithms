def quick_select(L, k):
    """
    Return the kth smallest element of UNSORTED list L,
    for k from 1 to len(L)

    input: An unsorted sequence S of n comparable
           elements together with an integer k∈[1,n].
    """
    import random

    if len(L) == 1:
        return L[0]

    pivot_item = random.choice(L)

    left = [x for x in L if x < pivot_item]
    mid = [x for x in L if x == pivot_item]
    right = [x for x in L if x > pivot_item]

    if k <= len(left):
        # kth smallest element resides in L
        return quick_select(left, k)
    elif k <= len(left) + len(mid):
        #kth smallest is equal to pivot
        return pivot_item
    else:
        # Compute a new selection parameter... kth smallest
        # is jth item in right
        j = k - len(left) - len(mid)
        return quick_select(right, j)
