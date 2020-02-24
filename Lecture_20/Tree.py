class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:

    def __init__(self):
        self.root = None

    def add(self, value):
        self.root = self.__add(value, self.root)

    def __add(self, value, node):

        if node is None:
            node = Node(value)
        else:

            if node.value > value:
                node.left = self.__add(value, node.left)
            if node.value < value:
                node.right = self.__add(value, node.right)

        return node

    def contains(self, item):
        return self.__contains(item, self.root)

    def __contains(self, item, node):

        if node is None:
            return False

        if node.value == item:
            return True

        if item < node.value:
            return self.__contains(item, node.left)
        elif item > node.value:
            return self.__contains(item, node.right)

    def display(self):
        self.__display(self.root)

    def __display(self, node, indent="", position="root"):

        if node is None:
            return

        print(indent, node.value, position)
        self.__display(node.left, indent + "\t", "left")
        self.__display(node.right, indent + "\t", "right")

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node is None:
            return 0

        left = self.__height(node.left)
        right = self.__height(node.right)

        return max(left, right) + 1


b = BST()

b.add(50)

b.add(30)

b.add(100)

b.add(101)

b.add(33)

b.add(29)

print(b.contains(33))

print(b.display())

print(b.height())
