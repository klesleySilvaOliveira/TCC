#teste = input("Pro favor, informe o caminho do arquivo: ")

# importing required modules
from zipfile import ZipFile
import json
  
# specifying the zip file name
file_name = "Scratch Project.sb3"
i = 0
  
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:  
    # extracting all the files
    print('Reading...')
    data = zip.read("project.json")
    jsonObj = json.loads(data)
    print(type(jsonObj))
    jsonFormattedStr = json.dumps(jsonObj, indent=4)
    print(jsonFormattedStr)
    target = jsonObj['monitors']
    print(target)
    #targets = json.loads(target)
    #for key in jsonObj:
    #  print(key, ":", jsonObj[key])
    print('Done!')
    print(len(data))
    while i < len(data):
      if data[i] == 98 and data[i+1] == 108:
       print("found one")
      
      i += 1