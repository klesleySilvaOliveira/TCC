# -*- coding: utf-8 -*-

class Block:
	def __init__(self, code, opcode, next, parent, inputs, fields, shadow, topLevel, indentation):
		self.code = code
		self.opcode = opcode
		self.next = next
		self.parent = parent
		self.inputs = inputs
		self.fields = fields
		self.shadow = shadow
		self.topLevel = topLevel
		self.indentation = indentation

	def get_opcode(self):
		return self.opcode

	def get_code(self):
		return self.code

	def get_next(self):
		return self.next

	def get_parent(self):
		return self.parent

	def get_inputs(self):
		return self.inputs

	def get_fields(self):
		return self.fields

	def get_indentation(self):
		return self.indentation