import itertools
from unittest import result

string = input("Digite a String a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))
