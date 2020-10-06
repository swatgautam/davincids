
class Node:
    def __init__(self,data_value):
        self.data = data_value
        self.left_child = None
        self.right_child = None
    

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert__(self,current_node, data_value):
        if current_node is None:
            return Node(data_value)
        if data_value < current_node.data:
            current_node.left_child = self.__insert__(current_node.left_child,data_value)
        if data_value > current_node.data:
            current_node.right_child = self.__insert__(current_node.right_child,data_value)
        return current_node

    def insert(self, data_value):
        self.root = self.__insert__(self.root, data_value)