#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")


import gtk
import gtk.glade
import time
import datetime
import pango
import serial
import Teclado


class MainWin:
    
    def __init__(self):
        
        self.widgets = gtk.glade.XML("Teclado1.glade")
        
        
        signals = { 
                    "gtk_main_quit" : gtk.main_quit }
                    
        
        
        self.widgets.signal_autoconnect(signals)
        
        self.entry1 = self.widgets.get_widget("entry1")
        
        self.button1 = self.widgets.get_widget("button1")
        self.button1.connect("clicked", self.uno,  None)
               
        self.button2 = self.widgets.get_widget("button2")
        self.button2.connect("clicked", self.dos,  None)
        
        self.button3 = self.widgets.get_widget("button3")
        self.button3.connect("clicked", self.tres, None)

        self.button4 = self.widgets.get_widget("button4")
        self.button4.connect("clicked", self.cuatro,  None)
               
        self.button5 = self.widgets.get_widget("button5")
        self.button5.connect("clicked", self.cinco,  None)
        
        self.button6 = self.widgets.get_widget("button6")
        self.button6.connect("clicked", self.seis, None)

        self.button7 = self.widgets.get_widget("button7")
        self.button7.connect("clicked", self.siete,  None)
               
        self.button8 = self.widgets.get_widget("button8")
        self.button8.connect("clicked", self.ocho,  None)
        
        self.button9 = self.widgets.get_widget("button9")
        self.button9.connect("clicked", self.nueve, None)

        self.button10 = self.widgets.get_widget("button10")
        self.button10.connect("clicked", self.cero,  None)
        
        self.button11 = self.widgets.get_widget("button11")
        self.button11.connect("clicked", self.punto, None)

        self.button12 = self.widgets.get_widget("button12")
        self.button12.connect("clicked", self.back,  None)
               
        self.button13 = self.widgets.get_widget("button13")
        self.button13.connect("clicked", self.clr,  None)
        
        self.button14 = self.widgets.get_widget("button14")
        self.button14.connect("clicked", self.ok, None)
        
        #textbuffer = TextBuffer(table=None)
        self.i = -1
        self.c = self.i-1
       
        
        
        
         
        
             

 
    def uno (self, widget, button1 ):
		
		self.entry1.append_text("1")
		self.i = self.i+1
		print(self.i)
		return
		
		
		
    def dos (self, widget, button2):
		self.entry1.append_text("2")
		self.i = self.i+1
		
		return

    def tres (self, widget, button3):
		
		self.entry1.append_text("3")
		self.i = self.i+1
		return
		
		
    def cuatro (self, widget, button4):
		
		self.entry1.append_text("4")
		self.i = self.i+1
		return
		  

    def cinco (self, widget, button5):
		
		self.entry1.append_text("5")
		self.i = self.i+1
		return
	
		
    def seis (self, widget, button6):
		
		self.entry1.append_text("6")
		self.i = self.i+1
		return
		
		
    def siete (self, widget, button7):
		
		self.entry1.append_text("7")
		self.i = self.i+1
		return

    def ocho (self, widget, button8):
		
		self.entry1.append_text("8")
		self.i = self.i+1
		return

    def nueve (self, widget, button9):
		
		self.entry1.append_text("9")
		self.i = self.i+1
		return

    def cero (self, widget, button10):
		
		self.entry1.append_text("0")
		self.i = self.i+1
		return

    def punto (self, widget, button11):
		global flag_punto
		global posicion
		self.entry1.append_text(".")
		self.i = self.i+1
		posicion = self.i
		print(posicion)
		self.button11.set_sensitive(False)
		flag_punto = True
		return 
		
    def back (self, widget, button12):
		global flag_punto
		global posicion
		
		print(self.i)
		if(self.i <= -1):
			self.i = -1
			print(self.i)
		else:
			self.entry1.delete_text(self.i, self.c)
			self.i = self.i-1
			print(self.i)
		
		if(self.i < posicion):
			self.button11.set_sensitive(True)
				
		return

    def clr (self, widget, button13):
		self.entry1.set_text("")
		self.i = -1
		self.button11.set_sensitive(True)
		
		
		return

    def ok (self, widget, button14):
		resultado = self.entry1.get_text()
		print(resultado)
		self.entry1.set_text ("")
		self.button11.set_sensitive(True)
		self.i = -1
		
		
		return


		
	
		

    

def main():
    gtk.main()

if __name__ == '__main__':
	
	MainWin() 
	main()
