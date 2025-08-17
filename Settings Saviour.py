#OPEN AN XML FILE AND PARSE IT
import xml.etree.ElementTree as ET

FileVal=input('Digite o nome do arquivo: ')

tree=ET.parse(FileVal)
#print('Debug: ', tree)

#RUN QUERIES
itemList=tree.findall('*')

#print('Debug',  itemList)

for i in itemList:
    print(i.text)

