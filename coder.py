import pickle
import numpy as np
import struct


class Huf_El(object):  # класс для таблицы частот

    def __init__(self, letter, code):
        self.letter = letter
        self.code = code


class Node(object):  # класс для дерева

    def __init__(self, letter, Hz, left_child, right_child):
        self.letter = letter
        self.Hz = Hz
        self.left_child = left_child
        self.right_child = right_child


"""читаем текст и делаем табличку"""

adress = 'C:\ForProg\qqq.txt'  # input()

Table = [Node(None, 0, None, None)]
i = 0

f = open(adress, 'r')
for char in f.read():
    i += 1
    if char == "¤" or char == "©":
        print(i)
    for j in range(len(Table)):
        if char == Table[j].letter:
            Table[j].Hz = Table[j].Hz + 1
            break
        if j == len(Table) - 1:
            print("new = ", char)
            Table.append(Node(char, 1, None, None))
            break

f.close()
print("END")

"""сортируем табличку"""

for i in range(len(Table)):
    for j in range(len(Table) - i - 1):
        if Table[j].Hz > Table[j + 1].Hz:
            z = Table[j]
            Table[j] = Table[j + 1]
            Table[j + 1] = z

for i in range(len(Table)):  # попадал 32 символ ASCII, хз что это и откуда, удаляю его и не парюсь)))
    if Table[i].Hz == 0:
        del Table[i]
        break

for i in range(len(Table)):
    print(Table[i].letter, " - ", Table[i].Hz)

i = 0
Table_letter_Copy = []
Table_Hz_Copy = []
for x in range(len(Table)):
    Table_letter_Copy.append(Table[x].letter)
    Table_Hz_Copy.append(Table[x].Hz)

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

all_bytes = 0

for i in range(len(Table)):
    for j in range(len(Code_Table)):
        if Table[i].letter == Code_Table[j].letter:
            all_bytes = all_bytes + ((Table[i].Hz * len(Code_Table[j].code)) / 8)

i = 0

Dictionary = dict()
print("DICTIONARY IS:")
for i in range(len(Code_Table)):
    Dictionary[Code_Table[i].letter] = Code_Table[i].code
    print(Code_Table[i].letter, " - ", Code_Table[i].code)

aspect_ratio = all_bytes / Table[-1].Hz

free_bits = -1
Code_Mass = []

"""C:\ForProg\_name_.txt"""

"""кодируем текст"""

FB = 0

counter = 0

f = open(adress, 'r')
for char in f.read():
    counter += 1
    for q in Dictionary[char]:
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


"запись шапки и массива в бинарник"
Cap = "C:\\ForProg\\user.dat"

counter = 0

for i in range(len(Table_letter_Copy)):
    p = ord(Table_letter_Copy[i])
    if p <= 255:
        counter = counter + 1

f = open(Cap, 'wb')
w = struct.pack('B', counter)  # struct.pack - для представления числа как байт
#  информацию о struct брал здесь : https://tirinox.ru/python-struct/
f.write(w)

for i in range(len(Table_letter_Copy)):
    p = ord(Table_letter_Copy[i])
    if p <= 255:
        w = struct.pack('B', p)
        f.write(w)
        w = struct.pack('I', Table_Hz_Copy[i])
        f.write(w)

i = 0
for i in range(len(Code_Mass)):
    w = struct.pack('B', Code_Mass[i])
    f.write(w)

w = struct.pack('b', FB)
f.write(w)

f.close()
"""C:\ForProg\qqq.txt"""


# 3202150

# 3202551
