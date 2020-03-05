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

"""читаем текст и делаем табличку"""

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

"""сортируем табличку"""

for i in range(len(Table)):
    for j in range(len(Table) - i - 1):
        if Table[j].Hz > Table[j + 1].Hz:
            z = Table[j]
            Table[j] = Table[j + 1]
            Table[j + 1] = z

Table_Copy = Table.copy()

i = 0

"""строим дерево"""

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
        Code_Table.append(Huf_El(child.letter, vector))


"""строим табличку с кодами символов"""

Table_Maker(Table[-1], vec)

free_bits = -1
Code_Mass = []

"""кодируем текст"""

FB = 0

f = open('C:\ForProg\qqq.txt', 'r')
for char in f.read():
    i = 0
    while char != Code_Table[i].letter:
        i = i + 1
    for q in Code_Table[i].code:
        if free_bits == -1:
            Code_Mass.append(0)
            free_bits = 7
            FB = free_bits
        if q == '1':
            Code_Mass[-1] = Code_Mass[-1] | (1 << free_bits)
            free_bits = free_bits - 1
            FB = free_bits
        else:
            free_bits = free_bits - 1
            FB = free_bits

f.close()

"""шапка"""

f = open('C:\ForProg\decode.txt', 'w')

for i in range(len(Table_Copy)):
    f.write(str(Table_Copy[i].letter))
    f.write(str(Table_Copy[i].Hz))
    f.write('\n')

f.close()

"""\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"""

f = open('C:\ForProg\decode.txt', 'r')

i = 0
v = 1
a = 1

Decode_Table = []

"""читаем шапку"""

for char in f.read():
    if char == '\n':
        v = 1
        i = i + 1
        a = 1
    if char != '\n':
        if v == 0:
            el = a * int(char)
            Decode_Table[i].Hz = Decode_Table[i].Hz + el
            a = a * 10
        if v == 1:
            Decode_Table.append(Node(char, 0, None, None))
            v = 0

i = 0

"""дерево"""

while i in range(len(Table) - 1):
    obj = Node(None, Decode_Table[i].Hz + Decode_Table[i + 1].Hz, Decode_Table[i], Decode_Table[i + 1])
    Decode_Table.append(obj)
    k = len(Decode_Table) - 1
    while Decode_Table[k].Hz <= Decode_Table[k - 1].Hz:
        x = Decode_Table[k]
        Decode_Table[k] = Decode_Table[k - 1]
        Decode_Table[k - 1] = x
        k = k - 1
    i = i + 2

i = 0
j = 0
obj = Decode_Table[-1]

"""декодирование с записью"""

f = open('C:\ForProg\decode.txt', 'a')
r = 0
y = 0

for i in range(len(Code_Mass)):
    if i == len(Code_Mass)-1:
        n = 8 - FB
    else:
        n = 8
    for j in range(n):
        a = Code_Mass[i] >> (7 - j) & 1
        if a == 0:
            obj = obj.left_child
            if obj.left_child is None:
                f.write(obj.letter)
                obj = Decode_Table[-1]
        if a == 1:
            obj = obj.right_child
            if obj.right_child is None:
                f.write(obj.letter)
                obj = Decode_Table[-1]
