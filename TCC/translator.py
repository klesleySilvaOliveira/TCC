# -*- coding: utf-8 -*-

# importing required modules
from DLinkedList import *
from blocks_classes import *
from functions import *
from files import *

# tradutor que recebe uma lista "DLinkedList" e traduz para Python
def translate(DLinkedList, json_obj):
	print("Código traduzido:")
	while True:
		if DLinkedList.get_size() < 1:
			return
		node = DLinkedList.pop_front()
		opCode = node.get_opcode()

		match opCode:
			case "event_whenflagclicked":
				string = ("print(\"O processo se iniciará quando a bandeira for clicada.\")")
				write(str(string))

			case "motion_movesteps":
				inputs = node.get_inputs()
				#print_formatted_json(inputs)
				string = ("print(\"O objeto moverá "+str(inputs['STEPS'][1][1])+" passos:\")")
				#print("for(i=0; i<", inputs['STEPS'][1][1], ";i++){print("passo")}")
				write(str(string))

			case "motion_turnleft":
				inputs = node.get_inputs()
				string = ("print(\"O objeto vira "+str(inputs['DEGREES'][1][1])+" graus à esquerda.\")")
				write(str(string))

			case "looks_think":
				inputs = node.get_inputs()
				string = ("print(\"O objeto pensa: "+str(inputs['MESSAGE'][1][1])+"\")")
				write(str(string))

			case "motion_turnright":
				inputs = node.get_inputs()
				string = ("print(\"O objeto vira "+str(inputs['DEGREES'][1][1])+" graus à direita.\")")
				write(str(string))


			case "looks_say":
				inputs = node.get_inputs()
				string = ("print(\"O objeto diz: "+str(inputs['MESSAGE'][1][1])+"\")")
				write(str(string))

			case "data_setvariableto":
				inputs = node.get_inputs()
				fields = node.get_fields()
				#print_formatted_json(inputs)
				string = (str(fields['VARIABLE'][0][0])+" = "+str(inputs['VALUE'][1][1]))
				write(str(string))

			case "control_repeat":
				inputs = node.get_inputs()
				#coloca novamente o 'node' na cabeça da lista, para seguir com o processo de adicionar os 'inputs' específicos do bloco
				DLinkedList.push_front(node)
				insert_by_code(json_obj, DLinkedList, inputs['SUBSTACK'][1], node.get_indentation())
				print(inputs['SUBSTACK'][1])
				DLinkedList.pop_front()

			# caso default
			case _:
				string = ('#Comando ainda não traduzido!')		