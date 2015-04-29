class HashMap(object):

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def put(self, key, value):
        """
        Add a new key-value pair to the map.
        If the key is already in the map then replace
        the old value with the new value
        """
        hash_pos = self.hash(key)

        self.slots[hash_pos] = key
        self.data[hash_pos] = value


    def get(self, key):

        hash_pos = self.hash(key)

        if hash_pos is not None:
            return self.data[hash_pos]



    def delete(self, key):

        hash_pos = self.hash(key)

        if hash_pos is not None:
            self.slots[hash_pos] = None
            self.data[hash_pos] = None



    def hash(self, key):
        hash_pos = self.modulo_ord_hash(key)

        if self.slots[hash_pos] is not None:

            #### Two scenarios ####

            # 1) If the hash_position corresponds
            #    to a key that is the SAME as the new key we're trying to hash,
            #    we'll use it and then just overrwrite the keyed position with
            #    its new value.
            #
            #    This apporoach also ensures that lookups can find a hash_pos
            #    for a particular key
            if self.slots[hash_pos] == key:
                return hash_pos

            # 2) If the hash_position is collides with a different key, we
            #    need to recompute it
            else:
                hash_pos = self.rehash(hash_pos)

        return hash_pos



    def __getitem__(self, key):
        return self.get(key)


    def __setitem__(self, key, data):
        return self.put(key, data)


    def modulo_ord_hash(self, key):
        """
        Hash based upon the ord value of a string

        NOTE: To prevent anagrams evaulating to the same
        ord total, each character is also given a weight for
        its position within the string
        """
        import random

        if not isinstance(key, str):
            key = str(key)

        res = 0
        for i in range(len(key)):
            res += ord(key[i]) + (random.randrange(i, len(key))) # weight based on position

        res = res % self.size
        return res


    def rehash(self, old_hash_pos):
        """
        Implementation of the quadratic probing method
        to resolve hash collisions
        """
        attempts = 0
        incrementor = 1

        while attempts < self.size:

            new_hash_pos = (old_hash_pos + incrementor) % self.size
            if self.slots[new_hash_pos] is None:
                return new_hash_pos

            attempts +=1
            incrementor += 2
