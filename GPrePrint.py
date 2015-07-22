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
    
    def __init__(self, uart, Lectora):
		
		
        
        self.widgets = gtk.glade.XML("GPrePrint.glade")
        
        
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
        self.entry1.modify_font(pango.FontDescription("sans 15"))
        
        self.entry4 = self.widgets.get_widget("entry4")
        self.entry4.modify_font(pango.FontDescription("sans 15"))
        
        self.entry3 = self.widgets.get_widget("entry3")
        self.entry3.modify_font(pango.FontDescription("sans 15"))
        
        self.entry2 = self.widgets.get_widget("entry2")
        self.entry2.modify_font(pango.FontDescription("sans 15"))
       
       
        
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
        self.button10.connect("clicked", self.cero,  None)
        
        self.button11 = self.widgets.get_widget("button11")
        self.button11.connect("clicked", self.punto, None)

        self.button12 = self.widgets.get_widget("button12")
        self.button12.connect("clicked", self.back,  None)
               
        #self.button13 = self.widgets.get_widget("button13")
        #self.button13.connect("clicked", self.clr,  None)
        
        self.button14 = self.widgets.get_widget("button14")
        self.button14.connect("clicked", self.ok, None)
        self.i = -1
        self.c = self.i-1
        
        
        
       
		
    def updates(self):
		self.statusbar1 = self.widgets.get_widget("statusbar1")
		context_id = self.statusbar1.get_context_id("data")
		self.push_item(context_id, time.strftime('Configuración	               	                                 %d, %b %Y  --  %H:%M'))
		     
		self.label3.set_text(uart.args)
		self.entry2.set_text(Lectora.args)
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
	
		dialog1 = KeyAdmin();
		run = dialog1.run()
		
		
		
    def uno (self, widget, button1):
		#global state1
		#global state2
		#state2 = button1
		self.entry1.append_text("1")
		self.i = self.i+1
		#self.button14.set_sensitive(state1 & state2)
		print 
		
		return
    def dos (self, widget, button2):
		#global state1
		#global state2
		#state2 = button2
		self.entry1.append_text("2")
		self.i = self.i+1
		#self.button14.set_sensitive(state1 & state2)
		return
		
    def tres (self, widget, button3):
		#global state1
		#global state2
		#state2 = button3
		self.entry1.append_text("3")
		self.i = self.i+1
		#self.button14.set_sensitive(state1 & state2)
		return
    def cuatro (self, widget, button4):
		#global state1
		#global state2
		#state2 = button4
		self.entry1.append_text("4")
		self.i = self.i+1
		#self.button14.set_sensitive(state1 & state2)
		return
    def cinco (self, widget, button5):
		#global state1
		#global state2
		#state2 = button5
		self.entry1.append_text("5")
		self.i = self.i+1
		#self.button14.set_sensitive(state1 & state2)
		return
    def seis (self, widget, button6):
		#global state1
		#global state2
		#state2 = button6
		self.entry1.append_text("6")
		self.i = self.i+1
		#self.button14.set_sensitive(state1 & state2)
		return
    def siete (self, widget, button7):
		#global state1
		#global state2
		#state2 = button7
		self.entry1.append_text("7")
		self.i = self.i+1
		#self.button14.set_sensitive(state1 & state2)
		return
    def ocho (self, widget, button8):
		#global state1
		#global state2
		#state2 = button8
		self.entry1.append_text("8")
		self.i = self.i+1
		#self.button14.set_sensitive(state1 & state2)
		return
    def nueve (self, widget, button9):
		#global state1
		#global state2
		#state2 = button9
		self.entry1.append_text("9")
		self.i = self.i+1
		#self.button14.set_sensitive(state1 & state2)
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
		self.button11.set_sensitive(False)
		flag_punto = True
		return
    def back (self, widget, button12):
		global flag_punto
		global posicion
		
		if(self.i <= -1):
			self.i = -1
			
		else:
			self.entry1.delete_text(self.i, self.c)
			self.i = self.i-1
			
		if(self.i < posicion):
			self.button11.set_sensitive(True)
			self.button14.set_sensitive(True)
			
		if (self.i == -1):
			self.button14.set_sensitive(False)
		if(self.i == posicion):
			self.button14.set_sensitive(False)
		
		return
		
    def clr (self, widget, button13):
		self.entry2.set_text("")
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
		
class lectora(threading.Thread):
	
	def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
		threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
		
		
		self.args = ""

		return
		
	def run(self):
		fp = open('/dev/ttyUSB0', 'rb')
		
		a = ""
		while True:
			buffer = fp.read(16)
			for c in buffer:
				if ord(c) > 0:
					a = a + c
					 
					if (c == "\n"):
						
						self.args = fp.read(16)
						print(self.args)
						a = ""
		fp.close()
		return 0
						
			
		
		
		
		
		
	
	
	

	
		
		

		

		


		
			
def main():
	
	

	gtk.main()
	

if __name__ == "__main__":
	global serial_1
	serial_1 = True

	
	uart = UART(args=())
	uart.start()
	
	Lectora = lectora(args=())
	Lectora.start()
	p = MainWin(uart, Lectora)	
	gtk.timeout_add(200, p.updates)
		
	gtk.gdk.threads_init()
	gtkt = threading.Thread(target=gtk.main, args=())
	gtkt.start()

	main()
	
	
	
	
	

    
   
		
   
    

 
    
    

