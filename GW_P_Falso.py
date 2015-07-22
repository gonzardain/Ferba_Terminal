#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import pygtk
pygtk.require("2.0")


import gtk
import gtk.glade
import time
import datetime
import pango
import serial
import threading
from Queue import Queue
from time import sleep
import sys


import RPi.GPIO as GPIO



class MainWin():
    
    def __init__(self, uart):
		
		
        
        self.widgets = gtk.glade.XML("GW_P.glade")
        
        
        signals = { 
                    "gtk_main_quit" : gtk.main_quit }
        
        
        
        uart.args
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        
        
        
        
        
        self.widgets.signal_autoconnect(signals)
        self.label1 = self.widgets.get_widget("label1")
        self.label1.modify_font(pango.FontDescription("sans 15"))
        self.label2 = self.widgets.get_widget("label2")
        self.label3 = self.widgets.get_widget("label3")
        self.label3.modify_font(pango.FontDescription("sans 15"))
        self.label7 = self.widgets.get_widget("label7")
        self.label7.modify_font(pango.FontDescription("sans 15"))
        self.label8 = self.widgets.get_widget("label8")
        self.label8.modify_font(pango.FontDescription("sans 15"))
        self.label9 = self.widgets.get_widget("label9")
        self.label9.modify_font(pango.FontDescription("sans 15"))
        self.entry1 = self.widgets.get_widget("entry1")
        self.entry4 = self.widgets.get_widget("entry4")
        self.entry3 = self.widgets.get_widget("entry3")
        self.entry2 = self.widgets.get_widget("entry2")
       
       
        
        self.button200 = self.widgets.get_widget("button200")
        self.button200.connect("clicked", self.clicked,  None)
               
        self.button100 = self.widgets.get_widget("button100")
        self.button100.connect("clicked", self.shutdown,  None)
        
        self.button1 = self.widgets.get_widget("button1")
        self.button1.connect("clicked", self.uno, True)
               
        self.button2 = self.widgets.get_widget("button2")
        self.button2.connect("clicked", self.dos,  True)
        
        self.button3 = self.widgets.get_widget("button3")
        self.button3.connect("clicked", self.tres, True)

        self.button4 = self.widgets.get_widget("button4")
        self.button4.connect("clicked", self.cuatro,  True)
               
        self.button5 = self.widgets.get_widget("button5")
        self.button5.connect("clicked", self.cinco,  True)
        
        self.button6 = self.widgets.get_widget("button6")
        self.button6.connect("clicked", self.seis, True)

        self.button7 = self.widgets.get_widget("button7")
        self.button7.connect("clicked", self.siete,  True)
               
        self.button8 = self.widgets.get_widget("button8")
        self.button8.connect("clicked", self.ocho,  True)
        
        self.button9 = self.widgets.get_widget("button9")
        self.button9.connect("clicked", self.nueve, True)

        self.button10 = self.widgets.get_widget("button10")
        self.button10.connect("clicked", self.cero,  True)
        
        self.button11 = self.widgets.get_widget("button11")
        self.button11.connect("clicked", self.punto, True)

        self.button12 = self.widgets.get_widget("button12")
        self.button12.connect("clicked", self.back,  True)
               
        self.button13 = self.widgets.get_widget("button13")
        self.button13.connect("clicked", self.clr,  True)
        
        self.button14 = self.widgets.get_widget("button14")
        self.button14.connect("clicked", self.ok, True)
        
        self.togglebutton1 = self.widgets.get_widget("togglebutton1")	#Boton tipo 1
        map = self.togglebutton1.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.togglebutton1.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.togglebutton1.set_style(style)
        self.togglebutton1.connect("clicked", self.t1, True)
        
        self.togglebutton2 = self.widgets.get_widget("togglebutton2")	#Boton tipo 2
        map = self.togglebutton2.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.togglebutton2.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.togglebutton2.set_style(style)
        self.togglebutton2.connect("clicked", self.t2, True)
        
        self.togglebutton3 = self.widgets.get_widget("togglebutton3")	#Boton tipo 3
        map = self.togglebutton3.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.togglebutton3.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.togglebutton3.set_style(style)
        self.togglebutton3.connect("clicked", self.t3, True)
        
        self.togglebutton4 = self.widgets.get_widget("togglebutton4")	#Boton tipo 4
        map = self.togglebutton4.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.togglebutton4.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.togglebutton4.set_style(style)
        self.togglebutton4.connect("clicked", self.t4, True)
        
        self.togglebutton5 = self.widgets.get_widget("togglebutton5")	#Boton tipo 5
        map = self.togglebutton5.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.togglebutton5.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.togglebutton5.set_style(style)
        self.togglebutton5.connect("clicked", self.t5, True)
        
        self.togglebutton6 = self.widgets.get_widget("togglebutton6")	#Boton tipo 6
        map = self.togglebutton6.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.togglebutton6.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.togglebutton6.set_style(style)
        self.togglebutton6.connect("clicked", self.t6, True)

        self.togglebutton7 = self.widgets.get_widget("togglebutton7")	#Boton tipo 7
        map = self.togglebutton7.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.togglebutton7.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.togglebutton7.set_style(style)
        self.togglebutton7.connect("clicked", self.t7, True)
        
        self.togglebutton8 = self.widgets.get_widget("togglebutton8")	#Boton tipo 8
        map = self.togglebutton8.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.togglebutton8.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.togglebutton8.set_style(style)
        self.togglebutton8.connect("clicked", self.t8, True)
        
        self.button14.set_sensitive(False)
        self.i = -1
        self.c = self.i-1

        
    def t8 (self, widget, togglebutton8):
		global state1
		self.entry2.set_text ("Tipo de Caja 8")
		state1 = togglebutton8
		self.button14.set_sensitive(state2 & state1)
		return
        
    def t7 (self, widget, togglebutton7):
		global state1
		self.entry2.set_text ("Tipo de Caja 7")
		state1 = togglebutton7
		self.button14.set_sensitive(state2 & state1)
		return
        
    def t6 (self, widget, togglebutton6):
		global state1
		self.entry2.set_text ("Tipo de Caja 6")
		state1 = togglebutton6
		self.button14.set_sensitive(state2 & state1)
		return

    def t5 (self, widget, togglebutton5):
		global state1
		self.entry2.set_text ("Tipo de Caja 5")
		state1 = togglebutton5
		self.button14.set_sensitive(state2 & state1)
		return       
        
        
    def t4 (self, widget, togglebutton4):
		global state1
		self.entry2.set_text ("Tipo de Caja 4")
		state1 = togglebutton4
		self.button14.set_sensitive(state2 & state1)
		return 
        
    def t3 (self, widget, togglebutton3):
		global state1
		self.entry2.set_text ("Tipo de Caja 3")
		state1 = togglebutton3
		self.button14.set_sensitive(state2 & state1)
		return 
        
    def t2 (self, widget, togglebutton2):
		global state1
		self.entry2.set_text ("Tipo de Caja 2")
		state1 = togglebutton2
		self.button14.set_sensitive(state2 & state1)
		return 
        
    def t1 (self, widget, togglebutton1):
		global state1
		self.entry2.set_text ("Tipo de Caja 1")
		state1 = togglebutton1	
		state1 = True
		print (state1, state2)
		self.button14.set_sensitive(state2 & state1)
		return
		
       
		
    def updates(self):
		self.statusbar1 = self.widgets.get_widget("statusbar1")
		context_id = self.statusbar1.get_context_id("data")
		self.push_item(context_id, time.strftime('Configuración	               	                                 %d, %b %Y  --  %H:%M'))
		        
		self.label3.set_text(uart.args)
		
		return True
	

    def push_item(self, data, prompt):
		try:
			context_id = self.statusbar1.get_context_id("data")
			
			self.pop_item(context_id)
		except:
			pass
		self.statusbar1.push(data, prompt)
		return
		         
    def update(self, hora):
		global ser

		
		
		if(GPIO.input(18) ==1):
			command = "/usr/bin/sudo shutdown -h now"
			import subprocess
			process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
			output = process.communicate()[0]
			print output 
			
		else:

			


			
			self.statusbar1 = self.widgets.get_widget("statusbar1")
			context_id = self.statusbar1.get_context_id("data")
			self.push_item(context_id, time.strftime('Configuración	               	                                 %d, %b %Y  --  %H:%M'))
		        
			return True

    def clicked (self, widget, button100):
	
		dialog1 = Calibration();
		run = dialog1.run()
		
		
		
    def uno (self, widget, button1):
		global state1
		global state2
		state2 = button1
		self.entry1.append_text("1")
		self.i = self.i+1
		self.button14.set_sensitive(state1 & state2)
		print (state1, state2)
		
		return
    def dos (self, widget, button2):
		global state1
		global state2
		state2 = button2
		self.entry1.append_text("2")
		self.i = self.i+1
		self.button14.set_sensitive(state1 & state2)
		return
		
    def tres (self, widget, button3):
		global state1
		global state2
		state2 = button3
		self.entry1.append_text("3")
		self.i = self.i+1
		self.button14.set_sensitive(state1 & state2)
		return
    def cuatro (self, widget, button4):
		global state1
		global state2
		state2 = button4
		self.entry1.append_text("4")
		self.i = self.i+1
		self.button14.set_sensitive(state1 & state2)
		return
    def cinco (self, widget, button5):
		global state1
		global state2
		state2 = button5
		self.entry1.append_text("5")
		self.i = self.i+1
		self.button14.set_sensitive(state1 & state2)
		return
    def seis (self, widget, button6):
		global state1
		global state2
		state2 = button6
		self.entry1.append_text("6")
		self.i = self.i+1
		self.button14.set_sensitive(state1 & state2)
		return
    def siete (self, widget, button7):
		global state1
		global state2
		state2 = button7
		self.entry1.append_text("7")
		self.i = self.i+1
		self.button14.set_sensitive(state1 & state2)
		return
    def ocho (self, widget, button8):
		global state1
		global state2
		state2 = button8
		self.entry1.append_text("8")
		self.i = self.i+1
		self.button14.set_sensitive(state1 & state2)
		return
    def nueve (self, widget, button9):
		global state1
		global state2
		state2 = button9
		self.entry1.append_text("9")
		self.i = self.i+1
		self.button14.set_sensitive(state1 & state2)
		return
    def cero (self, widget, button10):
	
		self.entry1.append_text("0")
		self.i = self.i+1
		return
    def punto (self, widget, button11):
		global flag_punto
		global posicion
		global posicion2
		self.entry1.append_text(".")
		self.i = self.i+1
		posicion = self.i
		posicion2 = self.i+1
		print (posicion2)
		self.button11.set_sensitive(False)
		flag_punto = True
		if(state1 & flag_punto == True):
			self.button14.set_sensitive(False)
		return
    def back (self, widget, button12):
		global flag_punto
		global posicion
		global posicion2
		
		if(self.i <= -1):
			
			self.i = -1
			
		else:
			self.entry1.delete_text(self.i, self.c)
			self.i = self.i-1
			print(self.i)
			
		if(self.i < posicion):
			self.button11.set_sensitive(True)
			self.button14.set_sensitive(True)
		if (self.i == -1):
			self.button14.set_sensitive(False)
		if(self.i == posicion):
			self.button14.set_sensitive(False)
			
			
			
			
		return
    def clr (self, widget, button13):
		self.entry1.set_text("")
		self.i = -1
		self.button11.set_sensitive(True)
		self.button14.set_sensitive(False)
		
		return
	
		
		
    def ok (self, widget, button14):
		Tipo = self.entry2.get_text()
		print(Tipo)
		resultado_num = float(self.entry1.get_text())
		resultado = str(resultado_num)
		self.entry4.set_text (resultado)
		self.entry3.set_text (time.strftime('%d, %b %Y  --  %H:%M'))
		self.entry1.set_text ("")
		self.button14.set_sensitive(False)
		file = open("newfile.txt", "w")
		file.write(resultado)
		file.write(time.strftime('%d, %b %Y  --  %H:%M'))
		file.write(Tipo)
		self.button11.set_sensitive(True)
		self.i = -1
		return
		
		
		
    def shutdown (self, widget, button200):
		
		command = "/usr/bin/sudo shutdown -h now"
		import subprocess 
		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]
		print output
	

		

		

	
	
	
class UART(threading.Thread):
	global ser
	global a

	
	
	def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
		threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
		global ser
		self.args = ""
	
		
		return 
		 
	def run (self):
		global a
		global serial_1
		#ser = serial.Serial ("/dev/ttyAMA0")
		

		while (serial_1):
			ser = serial.Serial ("/dev/ttyAMA0")
			ser.baudrate = 9600
			a = ser.read(13)
			ser.flush()
			ser.close()
			self.args = a
			
			
			time.sleep(.1)
		
		
		return 0


class Calibration():
	def __init__(self):
		self.gladefile = "Calibration.glade"
		
		
	def run(self):
		self.wTree = gtk.glade.XML(self.gladefile, "dialog1")
		self.dlg = self.wTree.get_widget("dialog1")
		
		
		self.button2 = self.wTree.get_widget("button2")
		self.button2.connect("clicked", self.op, None)
		self.result = self.dlg.run()
	
	def op(self, widget, button2):
		self.dlg.destroy()
		mainWindow = operation();
		run = mainWindow.run()
		return 

		
		
	

class operation():
	def __init__(self):
		self.widgets = gtk.glade.XML("Teclado.glade")
		signals = {			
								"gtk_main_quit" : gtk.main_quit }
								
							
		
	def run(self):
		
		self.entry1 = self.widgets.get_widget("entry1")
		
		self.button1 = self.widgets.get_widget("button1")
		self.button1.connect("clicked", self.uno, None)
		
		self.button2 = self.widgets.get_widget("button2")
		self.button2.connect("clicked", self.dos,  True)
		
		self.button3 = self.widgets.get_widget("button3")
		self.button3.connect("clicked", self.tres, True)
		
		self.button4 = self.widgets.get_widget("button4")
		self.button4.connect("clicked", self.cuatro,  True)
		
		self.button5 = self.widgets.get_widget("button5")
		self.button5.connect("clicked", self.cinco,  True)
		
		self.button6 = self.widgets.get_widget("button6")
		self.button6.connect("clicked", self.seis, True)
		
		self.button7 = self.widgets.get_widget("button7")
		self.button7.connect("clicked", self.siete,  True)
		
		self.button8 = self.widgets.get_widget("button8")
		self.button8.connect("clicked", self.ocho,  True)
		
		self.button9 = self.widgets.get_widget("button9")
		self.button9.connect("clicked", self.nueve, True)
		
		self.button10 = self.widgets.get_widget("button10")
		self.button10.connect("clicked", self.cero,  None)
		
		self.button11 = self.widgets.get_widget("button11")
		self.button11.connect("clicked", self.punto, None)
		
		self.button13 = self.widgets.get_widget("button13")
		self.button13.connect("clicked", self.delete,  None)
		
		self.button14 = self.widgets.get_widget("button14")
		self.button14.connect("clicked", self.ok, None)
		
		
		
		
		
		
		
	def uno(self, widget, button1):
		self.entry1.append_text("1")
		return
	
	def dos (self, widget, button2):
		self.entry1.append_text("2")
		return
	
	def tres (self, widget, button3):
		self.entry1.append_text("3")
		return
		
	def cuatro (self, widget, button4):
		self.entry1.append_text("4")
		return
		
	def cinco (self, widget, button5):
		self.entry1.append_text("5")
		return
	def seis (self, widget, button6):
		self.entry1.append_text("6")
		return
	
	def siete (self, widget, button7):
		self.entry1.append_text("7")
		return 
	
	def ocho (self, widget, button8):
		self.entry1.append_text("8")
		return
		
	def nueve (self, widget, button9):
		self.entry1.append_text("9")
		return
		
	def cero (self, widget, button10):
		self.entry1.append_text("0")
		return
		
	def punto (self, widget, button11):
		self.entry1.append_text(".")
		return 
		
	
	
	def ok (self, widget, button14):
		print("hjgjhgjhg")
		return
	
	def delete (self, widget, button13):
		self.entry1.set_text("")
		return 
		
		
	
		
	
		
			
	
	
	
	
		
	
		
		
		


		
			
def main():
	
	gtk.main()

if __name__ == "__main__":
	global serial_1
	serial_1 = True
	state1 = False
	state2 = False
	
	uart = UART(args=())
	uart.start()
	p = MainWin(uart)
		
	gtk.timeout_add(200, p.updates)
	gtk.gdk.threads_init()
	gtkt = threading.Thread(target=gtk.main, args=())
	gtkt.start()
	


	
	main()
	
	
	
	
	

    
   
		
   
    

 
    
    

