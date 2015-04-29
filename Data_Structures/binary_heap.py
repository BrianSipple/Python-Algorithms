class BinaryHeap(object):

    def __init__(self):
        self.items = [0]  # Initialize with unused zero to enable integer division in later methods
        self.size = 0


    def insert(self, item):

        self.items.append(item)
        self.size += 1
        self.percolateUp(self.size)  # Begin percolating at the end position


    def deleteMin(self):
        """
        The min is at the root, so we know what to delete.
        But... to maintain both heap structure and heap order....

        First, we will restore the root item by taking the last
        item in the list and moving it to the root position.
        Moving the last item maintains our heap structure property.

        However, we have probably destroyed the heap order property
        of our binary heap.

        Second, we will restore the heap order
        property by pushing the new root node down the tree to its
        proper position
        """
        returnVal = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self.size -= 1

        self.percolateDown(1)
        return returnVal



    def buildHeap(self, item_list):
        """
        Build a heap from scratch with when given a list of items
        """
        pos = len(item_list) // 2  # Because the heap is a complete binary tree, any nodes past the halfway point will be leaves and therefore have no children

        self.size = len(item_list)
        self.items = [0] + item_list[:]

        while (pos > 0):
            print(pos)

            self.percolateDown(pos)
            pos -= 1





######################### HELPERS ###########################

    def percolateUp(self, pos):
        """
        Helper for inserting items
        into the heap's tree structure in a way that
        allows us to regain the heap structure property
        by comparing the newly added item with its parent.

        If the newly added item is less than its parent,
        then we can swap the item with its parent
        """

        # The parent of the current node can be computed
        # by dividing the index of the current node by 2.
        parent_pos = pos // 2

        while parent_pos > 0:

            if self.items[pos] < self.items[parent_pos]:
                self.swap(parent_pos, pos)

            pos = parent_pos
            parent_pos = pos // 2



    def percolateDown(self, pos):

        while (pos*2) <= self.size:

            # Compare and swap withe the lesser of the children
            min_child_pos = self.minChildPos(pos)

            if self.items[pos] > self.items[min_child_pos]:
                self.swap(pos, min_child_pos)

            pos = min_child_pos






    def minChildPos(self, pos):
        """
        Returns the position of the min-valued child of a parent

        Right-child wins in a tie
        """
        if pos * 2 + 1 > self.size:   # The right child might not even exist if the end is the left
            return pos * 2

        left_c = self.items[pos*2]
        right_c = self.items[pos*2 + 1]

        if left_c < right_c:
            return pos*2
        else:
            return pos*2 + 1


    def swap(self, item_pos, with_pos):
        self.items[item_pos], self.items[with_pos] = self.items[with_pos], self.items[item_pos]
