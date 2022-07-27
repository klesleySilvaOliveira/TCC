# -*- coding: utf-8 -*-
# importa os arquivos necessários
from functions import *
from blocks_classes import *
from DLinkedList import *
from translator import *

lista = DLinkedList()

# recebe o caminho do arquivo desejado
file_path = input("Por favor, informe o caminho do arquivo: ")

# acessa os chars do endereço de ".sb3" até o fim da variável file_path e compara com o formato de scratch
if file_path[(file_path.find(".sb3")):] == ".sb3":
  print("Formato correto!")

# extrai os blocos referentes ao programa em scratch
json_obj = catch_blocks(file_path)

# transfere os objetos presentes no .json para uma lista de objetos 'Block'
lista = json_list_transfer(json_obj)

print_formatted_json(json_obj)

# tradutor que recebe uma lista "DLinkedList" e traduz para Python
translate(lista)

#lista.list_print()

#/home/klesley/Desktop/TCC/Scratch Project(2).sb3