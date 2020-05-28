import pickle
import struct


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


Decode_Table = []
Cap = "C:\\ForProg\\user.dat"
f = open(Cap, 'rb')
a = f.read(1)
s = struct.unpack('B', a)
print(s)
print(s)
for i in range(s[0]):
    code = struct.unpack('B', f.read(1))
    let = chr(code[0])
    z = f.read(4)
    numb = struct.unpack('I', z)
    Decode_Table.append(Node(let, numb[0], None, None))

# print(Decode_Table.l, " - ", Decode_Table.Hz)


Code_Mass = f.read()
FB = Code_Mass[-1]

i = 0

"""дерево"""

while i in range(len(Decode_Table) - 1):
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

for i in range(len(Code_Mass) - 1):
    if i == len(Code_Mass) - 2:
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
