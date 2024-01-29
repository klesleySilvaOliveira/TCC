# -*- coding: utf-8 -*-

# importing required modules
from DLinkedList import *
  
lista = DLinkedList()
lista.list_print()
print("Tamanho pré push front", lista.get_size())

lista.push_front(2)
lista.push_front(1)
print("Tamanho pós push front", lista.get_size())

lista.push_back(3)
lista.push_back(4)

print("Lista:")
lista.list_print()
print("Tamanho pós push back", lista.get_size())

lista.pop_front()
print("Lista pop front:")
lista.list_print()
print("Tamanho pós pop front", lista.get_size())

lista.pop_back()
print("Lista pop back:")
lista.list_print()
print("Tamanho pós pop back", lista.get_size())