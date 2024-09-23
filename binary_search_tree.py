# binary search tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        temp = self.root
        while temp:
            if value < temp.value:
                if temp.left is None:
                    temp.left = Node(value)
                    return
                else:
                    temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = Node(value)
                    return
                else:
                    temp = temp.right
            else:
                return

    def search(self, value):
        temp = self.root
        while temp:
            if value == temp.value:
                return temp
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return None


# use case
# Create a new binary search tree
bst = BinarySearchTree()

# Insert values into the binary search tree
values_to_insert = [50, 30, 70, 20, 40, 60, 80]
for value in values_to_insert:
    bst.insert(value)

# Search for values
search_values = [70, 25, 60]
for value in search_values:
    result = bst.search(value)
    if result:
        print(f"Value {value} found in the tree.")
    else:
        print(f"Value {value} not found in the tree.")
