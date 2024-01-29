# -*- coding: utf-8 -*-
# importing required modules
from zipfile import ZipFile
import json
from blocks_classes import *
from DLinkedList import *

# recebe um endereço de um arquivo .sb3 (Scratch 3) e retorna um objeto json
def catch_blocks(file_name):
	# opening the zip file in READ mode
	with ZipFile(file_name, 'r') as zip:  
	    # extracting all the files
	    print('Lendo o arquivo...')

	    #lê somente o arquivo "project.json" dentro do arquivo .sb3 e coloca no obj "data"
	    data = zip.read("project.json")

	    #carrega o conteúdo de "data" para o obj "jsonObj" e transforma em um objeto de classe "dict"
	    json_obj = json.loads(data)

	    # retorna um dicionário no formato Json contendo os blocos
	    return json_obj['targets'][1]['blocks']

# imprime na tela, de forma identada, um objeto json
def print_formatted_json(json_obj):
	print(json.dumps(json_obj, indent=4))

# transfere os objetos presentes no .json para uma lista de objetos 'Block'
def json_list_transfer(json_obj):
	# cria uma lista duplamente encadeada 'DLinkedList'
	lista = DLinkedList()

	# cria uma lista com as chaves presentes no json_obj
	keys_list = list(json_obj.keys())

	# adiciona a cabeça na lista
	for x in keys_list:
		if json_obj[x]['parent'] is None:

			# cria um objeto tipo 'Block' com os atributos alcançados pela variável 'x', atuando feito uma lista encadeada
			block = Block(x, 
				json_obj[x]['opcode'],
				json_obj[x]['next'],
				json_obj[x]['parent'],
				json_obj[x]['inputs'],
				json_obj[x]['fields'],
				json_obj[x]['shadow'],
				json_obj[x]['topLevel'],
				0)

			# adiciona o objeto 'block' no início da 'lista'
			lista.push_front(block)
			break

	# retira o último objeto da lista e cria uma imagem na variável 'node'
	node = lista.pop_back()

	# insere 'node' novamente na lista
	lista.push_back(node)

	# adiciona o atributo 'next' de 'node' na variável 'code' 
	code = node.get_next()

	rec_insert(json_obj, lista, code)

	return lista

#realiza, de forma recursiva, a inserção de itens e sub-itens na lista
def rec_insert(json_obj, lista, code):
	# cria um objeto tipo 'Block' com os atributos alcançados pela variável 'code', atuando feito uma lista encadeada
	block = Block(code, 
			json_obj[code]['opcode'],
			json_obj[code]['next'],
			json_obj[code]['parent'],
			json_obj[code]['inputs'],
			json_obj[code]['fields'],
			json_obj[code]['shadow'],
			json_obj[code]['topLevel'],
			0)

	# adiciona o objeto 'block' no fim da 'lista'
	lista.push_back(block)

	#condição de quebra de recursividade
	if block.get_next() is None:
		return
	else:
		rec_insert(json_obj, lista, block.get_next())

#insere em uma lista já pronta, uma sublista
def insert_by_code(json_obj, lista, code, indentacao):
	aux = code
	indenta = indentacao + 1

	while True:
		# cria um objeto tipo 'Block' com os atributos alcançados pela variável 'code', atuando feito uma lista encadeada
		block = Block(aux, 
				json_obj[aux]['opcode'],
				json_obj[aux]['next'],
				json_obj[aux]['parent'],
				json_obj[aux]['inputs'],
				json_obj[aux]['fields'],
				json_obj[aux]['shadow'],
				json_obj[aux]['topLevel'],
				indenta)

		# adiciona o objeto 'block' no fim da 'lista'
		lista.insert_by_code(block)

		# caso o parâmetro 'next' do objeto 'block' seja nulo, finaliza o loop
		if block.get_next() is None:
			return
		aux = block.get_next()