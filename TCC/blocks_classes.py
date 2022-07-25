# -*- coding: utf-8 -*-

class Block:
	def __init__(self, code, opcode, next, parent, inputs, fields, shadow, topLevel):
		self.code = code
		self.opcode = opcode
		self.next = next
		self.parent = parent
		self.inputs = inputs
		self.fields = fields
		self.shadow = shadow
		self.topLevel = topLevel

	def get_opcode(self):
		return self.opcode

	def get_code(self):
		return self.code

	def get_next(self):
		return self.next

	def get_parent(self):
		return self.parent