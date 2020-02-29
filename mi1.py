class Node(object):

    def __init__(self, letter, Hz, left_child, right_child):
        self.letter = letter
        self.Hz = Hz
        self.left_child = left_child
        self.right_child = right_child

    def fff(self):
        """ вывод """
        print(self.letter, " - ", self.Hz, self.left_child, self.right_child)


obj_1 = 5
obj_2 = 6
obj_3 = Node('x', 9, id(obj_1), id(obj_2))

obj_3.fff()
