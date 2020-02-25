class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1


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

            node.height = max(self.height(node.left), self.height(node.right)) + 1

        return self.__balance(node)

    def height(self, node):

        if node is None:
            return 0
        else:
            return node.height

    def display(self):
        self.__display(self.root)

    def __display(self, node, indent="", position="root"):

        if node is None:
            return

        print(indent, node.value, position, node.height, self.height(node.left) - self.height(node.right))
        self.__display(node.left, indent + "\t", "left")
        self.__display(node.right, indent + "\t", "right")

    def right_rotate(self):
        r = self.__right_rotate(self.root)
        self.root = r

    def __right_rotate(self, node):

        x = node
        y = x.left
        t1 = y.right

        x.right = y
        y.left = t1

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    def left_rotate(self):
        r = self.__left_rotate(self.root)
        self.root = r

    def __left_rotate(self, node):

        y = node
        x = y.right
        t2 = x.left

        x.left = y
        y.right = t2

        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def __balance(self, node):

        if (self.height(node.left) - self.height(node.right)) > 1:
            if (self.height(node.left.left) - self.height(node.left.right)) < 0:
                node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)

        elif (self.height(node.left) - self.height(node.right)) < -1:
            if (self.height(node.right.left) - self.height(node.right.right)) > 0:
                node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        return node

    def balanced(self):
        return self.__balanced(self.root)

    def __balanced(self, node):

        if node is None:
            return True

        current = abs(self.height(node.left) - self.height(node.right)) < 2
        left = self.__balanced(node.left)
        right = self.__balanced(node.right)

        return current and left and right


bs = BST()

bs.add(15)
bs.add(20)
bs.add(31)
bs.add(22)
bs.add(10)
bs.add(5)
bs.add(9)

bs.display()


print(bs.balanced())
print("")
bs.left_rotate()
bs.display()
print("")
bs.right_rotate()
bs.display()