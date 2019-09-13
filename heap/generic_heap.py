class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        # Insert at end of list
        self.storage.append(value)
        idx = len(self.storage)-1
        # place the value where it belongs
        self._bubble_up(idx)
        return self.storage

    def delete(self):
        # remove root
        return_value = self.storage[0]
        # put last element of list as the root
        element = self.storage.pop()
        if len(self.storage) == 0:
            return return_value
        # move root where it belongs
        self.storage[0] = element
        self._sift_down(0)
        return return_value

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        value = self.storage[index]
        while index >= 1:
            parentIdx = (index-1)//2
            parent = self.storage[parentIdx]
            if not self.comparator(value, parent):
                return
            self.storage[parentIdx] = value
            self.storage[index] = parent
            index = (index-1)//2

    def _sift_down(self, index):
        element = self.storage[index]
        while True:
            swap = None
            leftIdx = (2*index)+1
            if leftIdx <= len(self.storage)-1 and self.comparator(self.storage[leftIdx], element):
                swap = leftIdx
            rightIdx = (2*index)+2
            if rightIdx <= len(self.storage)-1 and self.comparator(self.storage[rightIdx], self.storage[leftIdx]):
                swap = rightIdx
            if swap != None:
                self.storage[index] = self.storage[swap]
                self.storage[swap] = element
            if swap != None:
                index = swap
            else:
                break
