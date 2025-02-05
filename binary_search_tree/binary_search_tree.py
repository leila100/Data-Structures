class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_value = BinarySearchTree(value)
        if self.value <= value:
            if self.right == None:
                self.right = new_value
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = new_value
            else:
                self.left.insert(value)
        return self

    def contains(self, target):
        if self.value == target:
            return True
        if target > self.value:
            if self.right == None:
                return False
            return self.right.contains(target)
        else:
            if self.left == None:
                return False
            return self.left.contains(target)

    def get_max(self):
        max_value = self.value
        if self.right == None:
            return max_value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
        return self
