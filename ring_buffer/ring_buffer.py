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
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current_index = 0
        # Boolean to mark whether all indices of list have been assigned
        self.list_full = False

    def append(self, item):
        self.storage[self.current_index] = item
        if self.current_index < self.capacity - 1:
            self.current_index += 1
        else:
            self.current_index = 0
            self.list_full = True

    def get(self):
        # list_full allows us to simply return storage if it is full, else it loops through the list to only include
        # non None values
        if self.list_full:
            return self.storage
        else:
            return [item for item in self.storage if item]


# This is as efficient as using a linked list because we never delete from storage and we keep track of the index
# so the runtime is constant.
