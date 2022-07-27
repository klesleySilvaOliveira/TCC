# -*- coding: utf-8 -*-

# importing required modules
from DLinkedList import *
from blocks_classes import *
from functions import *

# tradutor que recebe uma lista "DLinkedList" e traduz para Python
def translate(DLinkedList):
	print("Código traduzido:")
	while True:
		node = DLinkedList.pop_front()
		opCode = node.get_opcode()

		match opCode:
			case "event_whenflagclicked":
				print("print(\"O processo se iniciará quando a bandeira for clicada.\")")

			case "motion_movesteps":
				inputs = node.get_inputs()
				#print_formatted_json(inputs)
				print("print(\"O objeto moverá", inputs['STEPS'][1][1], "passos.\")")

			case "motion_turnleft":
				inputs = node.get_inputs()
				print("print(\"O objeto vira", inputs['DEGREES'][1][1], "graus à esquerda.\")")

			case "looks_think":
				inputs = node.get_inputs()
				print("print(\"O objeto pensa:", inputs['MESSAGE'][1][1], "\")")

			case "motion_turnright":
				inputs = node.get_inputs()
				print("print(\"O objeto vira", inputs['DEGREES'][1][1], "graus à direita.\")")


			case "looks_say":
				inputs = node.get_inputs()
				print("print(\"O objeto diz:", inputs['MESSAGE'][1][1], "\")")

			# caso default
			case _:
				print('#Comando ainda não traduzido!')

		if node.get_next() is None:
			break