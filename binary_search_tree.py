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
# Create a new binary search tree for managing employee salaries
salary_bst = BinarySearchTree()

# Insert employee salaries into the binary search tree
employee_salaries = [50000, 30000, 70000, 20000, 40000, 60000, 80000]
for salary in employee_salaries:
    salary_bst.insert(salary)

# Search for specific salaries to check if they exist in the system
search_salaries = [70000, 25000, 60000]
for salary in search_salaries:
    result = salary_bst.search(salary)
    if result:
        print(f"Salary ${salary} found in the system.")
    else:
        print(f"Salary ${salary} not found in the system.")




