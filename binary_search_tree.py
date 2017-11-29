
class Node:
    data = None
    right = None
    left = None
    parent = None

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent

    def min(self):
        node = self
        while node.right:
            node = node.right
        return node

    def max(self):
        node = self
        while node.left:
            node = node.left
        return node

class BST:
    root_node = None
    sorted_list = []
    def __init__(self, data):
        self.root_node = Node(data)

    def insert(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
        else:
            node = self.root_node
            parent_node = None
            while node:
                # insert to left if data is less than root_node
                if data > node.data:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(data, node)
                        return node.left
                        break

                # insert to left if data is greater than root_node
                if data < node.data:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(data, node)
                        return node.right
                        # break

        return node

    def traverse(self, node):
        """
        traverse tree
        :param node:
        :return:
        """
        # base case
        if node is None:
            return
        # start from right: smaller
        self.traverse(node.right)
        # current
        self.sorted_list.append(node.data)
        # end with left: larger
        self.traverse(node.left)

    def search(self, node, searched_node):

        if node is None:
            return False
        while node:
            if searched_node > node.data:
                node = node.left
            elif searched_node < node.data:
                node = node.right
            else:
                return node

        return False
        #

a = BST(11)
a.insert(9)
a.insert(101)
a.insert(90)
a.insert(70)
a.insert(8)
a.insert(5)
a.insert(4)
a.insert(7)
a.insert(3)
a.traverse(a.root_node)
print a.sorted_list
a_node = a.search(a.root_node, 3)
print a_node.parent.data

