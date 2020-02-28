from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Adds to list if under capacity
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        else:
            # sets current node value to item
            self.current.value = item
            # moves current to next node
            self.current = self.current.next
            # if current is none (tail has been reached) sets current to head
            if self.current is None:
                self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
