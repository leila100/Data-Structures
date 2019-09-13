class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Single_linked_List:
    def __init__(self):
        self.front = None
        self.back = None


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements? use linked list
        self.storage = Single_linked_List()

    # insert at the end of the linked list
    def enqueue(self, item):
        new_node = Node(item)
        if self.storage.front == None:
            self.storage.front = new_node
            self.storage.back = new_node
        else:
            self.storage.back.next = new_node
            self.storage.back = new_node
        self.size += 1
        return self

    # Remove from the from of the linked list
    def dequeue(self):
        if self.size == 0:
            return None
        return_value = self.storage.front.value
        if self.size == 1:
            self.storage.front = None
            self.storage.back = None
        else:
            self.storage.front = self.storage.front.next
        self.size -= 1
        return return_value

    def len(self):
        return self.size
