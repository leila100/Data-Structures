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
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
