#!/usr/bin/env python3
def backpack_algorithm(length, lista):
    if length == 0:
        return 0
    use_last = lista[-1] + remove(length-1, lista[:-1])
    use_first = lista[0] + remove(length-1, lista[1:])
    maximun = max(use_last, use_first)
    return maximun


def remove(length, lista):
    if length == 0:
        backpack_algorithm(0, lista)
    if str(lista) in dic:
        return dic[str(lista)]
    remove_last = backpack_algorithm(length-1, lista[:-1])
    remove_first = backpack_algorithm(length-1, lista[1:])
    maximun = max(remove_last, remove_first)
    dic[str(lista)] = maximun
    return maximun


length = int(input())
lista = [int(i) for i in input().split()]
dic = {}
print(backpack_algorithm(length, lista))
