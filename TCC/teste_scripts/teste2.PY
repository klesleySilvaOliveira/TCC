# -*- coding: utf-8 -*-
teste = input("Pro favor, informe o caminho do arquivo: ")

# importing required modules
from zipfile import ZipFile
import json
  
# specifying the zip file name
file_name = teste

# acessa os chars do endereço de ".sb3" até o fim da variável teste e compara com o formato de scratch
if teste[(teste.find(".sb3")):] == ".sb3":
  print("Formato correto!")

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:  
    # extracting all the files
    print('Reading...')
    #lê somente o arquivo "project.json" dentro do arquivo .sb3 e coloca no obj "data"
    data = zip.read("project.json")
    #carrega o conteúdo de "data" para o obj "jsonObj" e transforma em um objeto de classe "dict"
    jsonObj = json.loads(data)
    print(type(jsonObj))
    target = jsonObj['targets']
    print(type(target[0]))
    print(type(target[1]['blocks']))
    print(len(target[1]['blocks']))
    print(type(target[1]['blocks'].keys()))
    print(target[1]['blocks'].keys())
    #print(target[1]['blocks'])
    jsonFormattedStr = json.dumps(target[1]['blocks'], indent=4)
    print(jsonFormattedStr)
    for x in target[1]['blocks']:
      print(target[1]['blocks'][x]['opcode'])
      """jsonFormattedStr = json.dumps(target[1]['blocks'][x]['opcode'], indent=4)
      print(jsonFormattedStr)
      for x in range(0,10,1):
      print(x)
      /home/klesley/Desktop/TCC/Scratch Project.sb3"""