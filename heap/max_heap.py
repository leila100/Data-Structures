class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        idx = len(self.storage)-1
        while idx >= 1:
            parentIdx = (idx-1)//2
            parent = self.storage[parentIdx]
            if value <= parent:
                break
            self.storage[parentIdx] = value
            self.storage[idx] = parent
            idx = parentIdx
        return self.storage

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
