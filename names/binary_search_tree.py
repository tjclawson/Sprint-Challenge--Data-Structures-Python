import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value and self.right is not None:
            self.right.insert(value)
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
        elif value < self.value and self.left is not None:
            self.left.insert(value)
        elif value < self.value and self.left is None:
            self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        elif target > self.value and self.right is None:
            return False
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        elif target < self.value and self.left is None:
            return False



