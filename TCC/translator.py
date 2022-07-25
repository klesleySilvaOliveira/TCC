# -*- coding: utf-8 -*-

# importing required modules
from DLinkedList import *
from blocks_classes import *

# tradutor que recebe uma lista "DLinkedList" e traduz para Python
def translate(DLinkedList):
	print("Código traduzido:")
	while True:
		node = DLinkedList.pop_front()
		opCode = node.get_opcode()

		match opCode:
			case "event_whenflagclicked":
				print("event_whenflagclicked")

			case "motion_movesteps":
				print("motion_movesteps")

			case "motion_turnleft":
				print("motion_turnleft")

			case "looks_think":
				print("looks_think")

			case "motion_turnright":
				print("motion_turnright")

			case "looks_say":
				print("looks_say")

			# caso default
			case _:
				print('Comando ainda não traduzido!')

		if node.get_next() is None:
			break