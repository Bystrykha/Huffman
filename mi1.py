class Huf_El(object):

    def __init__(self, letter, code):
        self.letter = letter
        self.code = code


class Node(object):

    def __init__(self, letter, Hz, left_child, right_child):
        self.letter = letter
        self.Hz = Hz
        self.left_child = left_child
        self.right_child = right_child


obj_2 = Node
obj_3 = Node
obj_1 = Node(' ', 0, None, None)
obj_2 = Node('5', 7, id(obj_1), id(obj_3))
obj_3 = Node('x', 9, id(obj_1), id(obj_2))

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

f.close()

for i in range(len(Table)):
    for j in range(len(Table) - i - 1):
        if Table[j].Hz > Table[j + 1].Hz:
            z = Table[j]
            Table[j] = Table[j + 1]
            Table[j + 1] = z

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

Code_Table = []
vec = []


def Add_0(vector):
    a = vector.copy()
    a.append('0')
    return a


def Add_1(vector):
    a = vector.copy()
    a.append('1')
    return a


def Table_Maker(child, vector):
    if child.left_child is not None:
        Table_Maker(child.left_child, Add_0(vector))
        Table_Maker(child.right_child, Add_1(vector))
    if child.left_child is None:
        print(child.letter, vector)
        Code_Table.append(Huf_El(child.letter, vector))


Table_Maker(Table[-1], vec)
