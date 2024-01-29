# -*- coding: utf-8 -*-
# importing required modules
import os

#variavel global para reservar o nome do arquivo
file_name = ''

def change_my_dir():

	mydir = os.getcwd()
	results = '/results'

	if results in mydir:
		return

	mydir = mydir + results

	if not os.path.exists(mydir):
		os.makedirs(mydir)

	os.chdir(mydir)

	return

def lists_all_files():
	#se fez necessário usar sorted pois, se a lista não estiver ordenada, irá gerar erro caso já existam itens na pasta de forma desordenada
	return sorted(os.listdir(os.getcwd()))

def file_number():
	files = lists_all_files()
	x = 1

	for f in files:
		if f.__contains__(str(x)):
			print(x, " existe")
		else:
			return x
		
		x+=1

	return x

def get_a_file():
	global file_name
	if file_name == '':
		file_name = "result"+str(file_number())+".py"
		f = open(file_name, "x")
		f.close()
	return file_name

def write(string):
	change_my_dir()
	file_name = get_a_file()
	f = open(file_name, "a")
	f.write(string + '\n')
	f.close()
	return