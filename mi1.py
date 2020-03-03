import numpy as np
from collections import Counter


class Node(object):

    def __init__(self, letter, Hz, left_child, right_child):
        self.letter = letter
        self.Hz = Hz
        self.left_child = left_child
        self.right_child = right_child

    def fff(self):
        """ вывод """
        print(self.letter, "-", self.Hz, '\n')


obj_2 = Node
obj_3 = Node
obj_1 = Node(' ', 0, None, None)
obj_2 = Node('5', 7, id(obj_1), id(obj_3))
obj_3 = Node('x', 9, id(obj_1), id(obj_2))

# Table = [Node()]
i = 0
Table = [obj_1]

f = open('C:\ForProg\qqq.txt', 'r')
for char in f.read():
    for j in range(len(Table)):
        if char == Table[j].letter:
            Table[j].Hz = Table[j].Hz + 1
            break
        if j == len(Table) - 1:
            Table.append(Node(char, 1, None, None))
            break

for i in range(len(Table)):
    for j in range(len(Table) - i - 1):
        if Table[j].Hz > Table[j + 1].Hz:
            z = Table[j]
            Table[j] = Table[j + 1]
            Table[j + 1] = z

n = len(Table) - 1

i = 0
while i in range(len(Table) - 1):
    obj = Node(None, Table[i].Hz + Table[i + 1].Hz, Table[i], Table[i + 1])
    Table.append(obj)
    k = len(Table) - 1
    while Table[k].Hz <= Table[k - 1].Hz:
        x = Table[k]
        Table[k] = Table[k - 1]
        Table[k - 1] = x
        k = k - 1
    i = i + 2


class Huf_El(object):

    def __init__(self, letter, code):
        self.letter = letter
        self.code = code


vec = []

child = Table[len(Table) - 1]
parent = Node
Parents = []
i = 0
HuffTab = []

print(1)


def Table_Maker(descendant, ancestor, index, Ancestors, vector, HF):
    """шаг в лево"""
    if descendant.left_child is not None:
        print(1)
        while descendant.left_child is not None:
            ancestor = descendant
            Ancestors.append(ancestor)
            descendant = descendant.left_child
            vector.append('0')
    if descendant.left_child is None:
        """нашли левый крайний"""
        print(2)
        vector.append('0')
        HF.append(Huf_El(descendant.letter, vector))
        index = index + 1
        if index == n:
            return HF
        descendant = ancestor
        Ancestors.pop()
        ancestor = Ancestors[-1]
        vector.pop()
    if descendant.right_child is not None:
        """шаг в право"""
        print(3)
        ancestor = descendant
        Ancestors.append(ancestor)
        descendant = descendant.right_child
        vector.append('1')
        Table_Maker(descendant, ancestor, index, Ancestors, vector, HF)
    if descendant.right_child is None:
        """нашли правый крайний элемент"""
        print(4)
        vector.append('1')
        HF.append(Huf_El(descendant.letter, vector))
        index = index + 1
        if index == n:
            return HF
        while descendant.left_child is None:
            print(5)
            descendant = ancestor
            Ancestors.pop()
            ancestor = Ancestors[-1]
            vector.pop()
        if descendant.right_child is not None:
            ancestor = descendant
            Ancestors.append(ancestor)
            descendant = descendant.right_child
            vector.append('1')
            Table_Maker(descendant, ancestor, index, Ancestors, vector, HF)


HuffTab = Table_Maker(child, parent, i, Parents, vec, HuffTab)
