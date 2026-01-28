class Binary_tree_builder:
    def build_tree(self, elements):
        if len(elements) == 1:
            return Binary_tree(elements[0])
        self.elements = sorted(elements)
        root = elements[len(self.elements) // 2]
        left = elements[:len(self.elements) // 2]
        right = elements[len(self.elements) // 2:]
        return Binary_tree(root, self.build_tree(left), self.build_tree(right))

class Binary_tree:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    #TODO: _balance() function to fix linear branches after addition

    def add(self, item):
        if self.root is None:
            self.root = Binary_tree(item)
            return

        if self.root == item:
            print("Item already present")
            return

        if item < self.root:
            if self.left is None:
                self.left = Binary_tree(item)
                return
            else:
                self.left.add(item)
        if item > self.root:
            if self.right is None:
                self.right = Binary_tree(item)
                return
            else:
                self.right.add(item)

    def search(self, item):
        if self.root is None:
            return
        if self.root == item:
            print("Item found")
            return self.root
        else:
            if item < self.root:
                if self.left is None:
                    return
                self.left.search(item)
            else:
                if self.right is None:
                    return
                self.right.search(item)

    def _delete_item(self, item):
        if self.root is None:
            return
        if self.root == item:
            self.root = None
            return
        if item < self.root:
            self.left.delete(item)
        else:
            self.right.delete(item)

    def _fill_gaps(self):
        if self.root is None:
            if self.right is not None:
                self.root = self.right.root
                self.right.root = None
                self.right._fill_gaps()
                return
            elif self.left is not None:
                self.root = self.left.root
                self.left.root = None
                self.left._fill_gaps()
                return
        else:
            if self.left is not None:
                self.left._fill_gaps()
                return
            if self.right is not None:
                self.right._fill_gaps()
                return

    def delete(self, item):
        self._delete_item(item)
        self._fill_gaps()

if __name__ == "__main__":
    elements = [1, 2, 3, 4, 6, 8, 9]
    tree_builder = Binary_tree_builder()
    binary_tree = tree_builder.build_tree(elements)

    binary_tree.search(6)
    binary_tree.search(5)
    binary_tree.add(8)
    binary_tree.add(10)
    binary_tree.search(10)
    binary_tree.delete(8)
    binary_tree.search(8)
    binary_tree.search(10)
    binary_tree.search(9)