#!/usr/bin/env python
# -*- coding: utf-8 -*-



import elementtree.ElementTree as ET

tree = ET.parse("Settings.xml")

a = tree.findtext("WorkingStrategy")
b = tree.findtext("WeightStrategy")


def weightprint():
        print("Modo de trabajo: Weight & Print Activado")

def preprint():
         print("Modo de trabajo: Pre-Print Activado") 

Modos1 = {"0" : weightprint,
         "1" : preprint
        }

dic1 = Modos1[a]
dic1()

def Auto():
    print("Modo de pesado: Auto Activado")

def Given():
    print("Modo de pesado: Given Activado")

def Scales():
    print("Modo de pesado: Scales Activado")

Modos2 = { "0" : Auto,
           "1" : Given,
           "2" : Scales
          }
dic2 = Modos2[b]
dic2()

     
root = tree.getroot()
#tree.write("out.xml")
