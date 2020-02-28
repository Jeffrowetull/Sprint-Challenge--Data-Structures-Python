from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        start = self.current
        list_buffer_contents.append(start.value)
        if start.next:
            n = start.next
        else:
            n = self.storage.head
        while n != start:
            list_buffer_contents.append(n.value)
            if n.next:
                n = n.next
            else:
                n = self.storage.head

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.current = -1
        self.storage = [None] * capacity

    def append(self, item):
        self.current += 1
        if self.current == len(self.storage):
            self.current = 0
        self.storage[self.current] = item

    def get(self):
        return [x for x in self.storage if x is not None]
