class UFPartition(object):
    """
    Union-find partition data structure.

    Provides a sequence-based partition consisting of unique
    Groups that can be used to manage disjoint sets (e.g, when
    computing the minimum spanning tree in a graph using Kruskal's
    algorithm)
    """
    class Position(object):

        def __init__(self, key, data):
            self._key = key
            self._data = data
            self._size = 1
            self._parent = self   # convention for a group leader

        def data(self):
            """
            Return data stored at this Position
            """
            return self._data


    def make_group(self, data):
        """
        Makes a new group containing a data item and returns its postion
        """
        return self.Position(self, data)


    def find(self, p):
        """
        Finds the group containing p and returns the Position
        of its leader
        """
        if self._parent != p:
            p._parent = self.find(p._parent) # overwrite p._parent after recursion
            return p._parent


    def union(self, p, q):
        """
        Merges the groups containing a and b (if distinct)
        """
        a_group = self.find(p)
        b_group = self.find(q)

        if a_group is not b_group:
            if a_group._size > b_group._size:
                b_group._parent = a_group
                a_group._size += b_group._size
            else:
                a_group._parent = b_group
                b_group._size += a_group._size
