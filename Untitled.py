# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
tree = ET.ElementTree(file='Operators.xml')
root = tree.getroot()


try:
    a=int(raw_input("Define el tipo de operador:"))
except ValueError:
    print "tipo no Válido"

try:
    b=str(raw_input("Escribe el nombre del Operador:"))
except ValueError:
          print "Nombre no valido"

    

for Type in root.iter("Type"):
    new_Type = a
    Type.text = str(new_Type)
    

for GivenName in root.iter("GivenName"):
          new_GivenName = b
          GivenName.text = str(new_GivenName)
          
          
    

tree.write("Operators2.xml")




