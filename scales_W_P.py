#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#
#   Nombre del Programa scales_W_P.py
#   Resumen:
#
#
#   Autor: ALT Ingeniería
#
#
#


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
import bascula
from collections import Counter
import math
GPIO.setwarnings(False)
global b
global m

class ventana_principal():
    
    def __init__(self, leer_operador, obtener_peso):

        self.widgets = gtk.glade.XML("scales_W_P1.glade")
        
        
        signals = { 
                    "destroy" : gtk.main_quit}

        leer_operador.args
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


        self.widgets.signal_autoconnect(signals)
        
        self.mainWindow = self.widgets.get_widget("mainWindow")

			
          
########################################################################################################################
        #Inicialización de etiquetas
########################################################################################################################
        self.etiqueta_pesoActual = self.widgets.get_widget("etiqueta_pesoActual")
        self.etiqueta_pesoActual.modify_font(pango.FontDescription("sans 15"))
        self.etiqueta_TipoCaja = self.widgets.get_widget("etiqueta_TipoCaja")
        self.etiqueta_TipoCaja.modify_font(pango.FontDescription("sans 15"))
        self.etiqueta_peso = self.widgets.get_widget("etiqueta_peso")
        self.etiqueta_peso.modify_font(pango.FontDescription("sans 15"))
        self.etiqueta_FechaHora = self.widgets.get_widget("etiqueta_FechaHora")
        self.etiqueta_FechaHora.modify_font(pango.FontDescription("sans 15"))
        self.etiqueta_IDoperator = self.widgets.get_widget("etiqueta_IDoperator")
        self.etiqueta_IDoperator.modify_font(pango.FontDescription("sans 15"))
########################################################################################################################
        #Inicialización de Indicadores
########################################################################################################################
        self.indicador_PesoActual = self.widgets.get_widget("indicador_PesoActual")
        self.indicador_PesoActual.modify_font(pango.FontDescription("sans 20"))
        self.indicador_Peso = self.widgets.get_widget("indicador_Peso")
        self.indicador_FechaHora = self.widgets.get_widget("indicador_FechaHora")
        self.indicador_TipoCaja = self.widgets.get_widget("indicador_TipoCaja")
########################################################################################################################
        #inicialización de botones
########################################################################################################################
        self.Boton_Menu = self.widgets.get_widget("Boton_Menu")
        self.Boton_Menu.connect("clicked", self.abrir_menu,  None)
        self.Boton_Apagar = self.widgets.get_widget("Boton_Apagar")
        self.Boton_Apagar.connect("clicked", self.shutdown,  None)
        self.boton_caja1 = self.widgets.get_widget("boton_caja1")	#Boton tipo 1
        map = self.boton_caja1.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.boton_caja1.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.boton_caja1.set_style(style)
        self.boton_caja1.connect("clicked", self.activar_caja1, True)
        self.boton_caja2 = self.widgets.get_widget("boton_caja2")	#Boton tipo 2
        map = self.boton_caja2.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.boton_caja2.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.boton_caja2.set_style(style)
        self.boton_caja2.connect("clicked", self.activar_caja2, True)
        self.boton_caja3 = self.widgets.get_widget("boton_caja3")	#Boton tipo 3
        map = self.boton_caja3.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.boton_caja3.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.boton_caja3.set_style(style)
        self.boton_caja3.connect("clicked", self.activar_caja3, True)
        self.boton_caja4 = self.widgets.get_widget("boton_caja4")	#Boton tipo 4
        map = self.boton_caja4.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.boton_caja4.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.boton_caja4.set_style(style)
        self.boton_caja4.connect("clicked", self.activar_caja4, True)
        self.boton_caja5 = self.widgets.get_widget("boton_caja5")	#Boton tipo 5
        map = self.boton_caja5.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.boton_caja5.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.boton_caja5.set_style(style)
        self.boton_caja5.connect("clicked", self.activar_caja5, True)
        self.boton_caja6 = self.widgets.get_widget("boton_caja6")	#Boton tipo 6
        map = self.boton_caja6.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.boton_caja6.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.boton_caja6.set_style(style)
        self.boton_caja6.connect("clicked", self.activar_caja6, True)
        self.boton_caja7 = self.widgets.get_widget("boton_caja7")	#Boton tipo 7
        map = self.boton_caja7.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.boton_caja7.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.boton_caja7.set_style(style)
        self.boton_caja7.connect("clicked", self.activar_caja7, True)
        self.boton_caja8 = self.widgets.get_widget("boton_caja8")	#Boton tipo 8
        map = self.boton_caja8.get_colormap()
        color = map.alloc_color("Yellow")
        style = self.boton_caja8.get_style().copy()
        style.bg[gtk.STATE_ACTIVE] = color
        self.boton_caja8.set_style(style)
        self.boton_caja8.connect("clicked", self.activar_caja8, True)
########################################################################################################################
    # Funciones de la ventana principal
########################################################################################################################
    def activar_caja8 (self, widget, boton_caja8):
		global state1
		status = self.boton_caja8.get_active()
		if(status == True):	
			self.indicador_TipoCaja.set_text ("Tipo de Caja 8")
			state1 = boton_caja8
			self.boton_caja1.set_active(False)
			self.boton_caja2.set_active(False)
			self.boton_caja3.set_active(False)
			self.boton_caja4.set_active(False)
			self.boton_caja5.set_active(False)
			self.boton_caja6.set_active(False)
			self.boton_caja7.set_active(False)
		else:
			return		

		return

    def activar_caja7 (self, widget, boton_caja7):
		global state1
		status = self.boton_caja7.get_active()
		if(status == True):	
			self.indicador_TipoCaja.set_text ("Tipo de Caja 7")
			state1 = boton_caja7
			self.boton_caja1.set_active(False)
			self.boton_caja2.set_active(False)
			self.boton_caja3.set_active(False)
			self.boton_caja4.set_active(False)
			self.boton_caja5.set_active(False)
			self.boton_caja6.set_active(False)
			self.boton_caja8.set_active(False)
		else:
			return

		return

    def activar_caja6 (self, widget, boton_caja6):
		global state1
		status = self.boton_caja6.get_active()
		if(status == True):	
			self.indicador_TipoCaja.set_text ("Tipo de Caja 6")
			state1 = boton_caja6
			self.boton_caja1.set_active(False)
			self.boton_caja2.set_active(False)
			self.boton_caja3.set_active(False)
			self.boton_caja4.set_active(False)
			self.boton_caja5.set_active(False)
			self.boton_caja7.set_active(False)
			self.boton_caja8.set_active(False)
		else:
			return
		return

    def activar_caja5 (self, widget, boton_caja5):
		global state1
		status = self.boton_caja5.get_active()
		if(status == True):	
			self.indicador_TipoCaja.set_text ("Tipo de Caja 5")
			state1 = boton_caja5
			self.boton_caja1.set_active(False)
			self.boton_caja2.set_active(False)
			self.boton_caja3.set_active(False)
			self.boton_caja4.set_active(False)
			self.boton_caja6.set_active(False)
			self.boton_caja7.set_active(False)
			self.boton_caja8.set_active(False)
		else:
			return		

		return


    def activar_caja4 (self, widget, boton_caja4):
		global state1
		status = self.boton_caja4.get_active()
		if(status == True):		
			self.indicador_TipoCaja.set_text ("Tipo de Caja 4")
			state1 = boton_caja4
			self.boton_caja1.set_active(False)
			self.boton_caja2.set_active(False)
			self.boton_caja3.set_active(False)
			self.boton_caja5.set_active(False)
			self.boton_caja6.set_active(False)
			self.boton_caja7.set_active(False)
			self.boton_caja8.set_active(False)
		else:
			return			

		return

    def activar_caja3 (self, widget, boton_caja3):
		global state1
		status = self.boton_caja3.get_active()
		if(status == True):
			self.indicador_TipoCaja.set_text ("Tipo de Caja 3")
			state1 = boton_caja3
			self.boton_caja1.set_active(False)
			self.boton_caja2.set_active(False)
			self.boton_caja4.set_active(False)
			self.boton_caja5.set_active(False)
			self.boton_caja6.set_active(False)
			self.boton_caja7.set_active(False)
			self.boton_caja8.set_active(False)
		else:
			return 		

		return

    def activar_caja2 (self, widget, boton_caja2):
		global state1
		status = self.boton_caja2.get_active()
		if(status == True):
			self.indicador_TipoCaja.set_text ("Tipo de Caja 2")
			state1 = boton_caja2
			self.boton_caja1.set_active(False)
			self.boton_caja3.set_active(False)
			self.boton_caja4.set_active(False)
			self.boton_caja5.set_active(False)
			self.boton_caja6.set_active(False)
			self.boton_caja7.set_active(False)
			self.boton_caja8.set_active(False)			
		
		else:
			return
			
		return

    def activar_caja1 (self, widget, boton_caja1):
		global state1
		status = self.boton_caja1.get_active()
		if(status == True):
			self.indicador_TipoCaja.set_text ("Tipo de Caja 1")
			state1 = boton_caja1
			self.boton_caja2.set_active(False)
			self.boton_caja3.set_active(False)
			self.boton_caja3.set_active(False)
			self.boton_caja5.set_active(False)
			self.boton_caja6.set_active(False)
			self.boton_caja7.set_active(False)
			self.boton_caja8.set_active(False)
		else:
			return 
			
		return

    def updates(self):

        if(GPIO.input(18) ==1):
            command = "/usr/bin/sudo shutdown -h now"
            import subprocess
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            print output
        else:

		    self.statusbar1 = self.widgets.get_widget("statusbar1")
		    context_id = self.statusbar1.get_context_id("data")
		    self.escribir_estado(context_id, time.strftime('Configuración	               	                             %d, %b %Y  --  %H:%M'))

		    self.etiqueta_IDoperator.set_text(leer_operador.args)
		    self.indicador_PesoActual.set_text(obtener_peso.args)
		    self.indicador_Peso.set_text(obtener_peso.high)
		    if(obtener_peso.flag == True):

			   self.indicador_FechaHora.set_text(time.strftime('%d, %b %Y  --  %H:%M'))
		    return True

    def escribir_estado(self, data, prompt):
		try:
			context_id = self.statusbar1.get_context_id("data")

			self.pop_item(context_id)
		except:
			pass
		self.statusbar1.push(data, prompt)
		return
    
    def abrir_menu (self, widget, Boton_Menu):

		dialog1 = Calibration();
		run = dialog1.run()

    def shutdown (self, widget, Boton_Apagar):
		
		command = "/usr/bin/sudo shutdown -h now"
		import subprocess 
		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]
		print output

class leer_operador(threading.Thread):
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
		
class obtener_peso(threading.Thread):
	global b
	global m
	
	def __init__(self, group=None, target=None, name=None, args=(), high=(), flag=(), kwargs=None, verbose=None):
		threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
		self.args = ""
		self.high = ""
		self.flag = False
		return
		
	def run (self):
		
		limh = 2
		max1 = limh
		flaglim = 0
		#print("peso")

		#while (GPIO.input(06) == False):
		cont = 0
		
		while(True):
			#cont = cont + 1
			
			self.flag = False
			limh = float(2.0)
			adc_flag, adc_raw = bascula.leer_ADC()
			
			
			
			if(adc_flag == True):
				#cosa = bascula.escalar_Peso(m, b, adc_raw)
				cosa = bascula.filtrar_ADC(Parametros_filtro, peso_escalado)
				
				if (cosa > max1 and flaglim == 1):
					max1 = cosa
				if (cosa <= limh and flaglim == 1):
					#print(max1)
					self.flag = True
					cosa3 = str(max1)
					self.high = cosa3[:3]
					flaglim = 0
					max1 = limh
					#print(self.flag)
					time.sleep(1)
				
				if (cosa >= limh and flaglim == 0):
					flaglim = 1
				cosa1 = str(cosa)
				#print(cosa1)
				self.args = cosa1[:4]
				


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
	global b
	global m
	def __init__(self):
		
		self.widgets = gtk.glade.XML("Calibration2.glade")
		signals = {			
								"gtk_main_quit" : gtk.main_quit }
								
							
		
	def run(self):
		self.window1 = self.widgets.get_widget("window1")
		self.indicador_PesoConocido = self.widgets.get_widget("indicador_PesoConocido")

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

		self.button12 = self.widgets.get_widget("button12")
		self.button12.connect("clicked", self.delete,  None)
		
		self.button13 = self.widgets.get_widget("button13")
		self.button13.connect("clicked", self.borrar_texto,  None)

		self.button14 = self.widgets.get_widget("button14")
		self.button14.connect("clicked", self.obtener_punto1, None)
		
		self.button15 = self.widgets.get_widget("button15")
		self.button15.connect("clicked", self.guardar_calibracion, None)
		self.button15.set_sensitive(False)
		
		self.button17 = self.widgets.get_widget("button17")
		self.button17.connect("clicked", self.obtener_punto2, None)
		
		self.button16 = self.widgets.get_widget("button16")
		self.button16.connect("clicked", self.reiniciar_calibracion, None)
		
		self.button140 = self.widgets.get_widget("button140")
		self.button140.connect("clicked", self.cancelar_calibracion, None)
		
		self.i = -1
		self.c = self.i-1
		self.button17.set_sensitive(False)
		
	def uno(self, widget, button1):
		self.indicador_PesoConocido.append_text("1")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return
	
	def dos (self, widget, button2):
		self.indicador_PesoConocido.append_text("2")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return
	
	def tres (self, widget, button3):
		self.indicador_PesoConocido.append_text("3")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return
		
	def cuatro (self, widget, button4):
		self.indicador_PesoConocido.append_text("4")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return
		
	def cinco (self, widget, button5):
		self.indicador_PesoConocido.append_text("5")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return
	def seis (self, widget, button6):
		self.indicador_PesoConocido.append_text("6")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return
	
	def siete (self, widget, button7):
		self.indicador_PesoConocido.append_text("7")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return 
	
	def ocho (self, widget, button8):
		self.indicador_PesoConocido.append_text("8")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return
		
	def nueve (self, widget, button9):
		self.indicador_PesoConocido.append_text("9")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return
		
	def cero (self, widget, button10):
		self.indicador_PesoConocido.append_text("0")
		self.i = self.i+1
		self.button17.set_sensitive(True)
		return
		
	def punto (self, widget, button11):
		global flag_punto
		global posicion
		self.indicador_PesoConocido.append_text(".")
		self.i = self.i+1
		posicion = self.i
		self.button11.set_sensitive(False)
		self.button17.set_sensitive(False)
		flag_punto = True
		return 
		
	
	def obtener_punto1 (self, widget, button14):
		global b_posible
		
		bascula.ini_ADC()
		array_lecturaADC = []
		cont = 0
		while (cont < 10):
			adc_flag, adc_raw = bascula.leer_ADC()
			if(adc_flag == True):
				array_lecturaADC.append(adc_raw)
				punto_x2 = sum(array_lecturaADC[2:])/float(8)
				cont = cont + 1
		punto_x1 = 0
		b_posible = punto_x2
		print(array_lecturaADC[2:])
		print(b)

		return 

	def obtener_punto2 (self, widget, button17):
		global m_posible
		bascula.ini_ADC()
		array_lecturaADC = []
		cont = 0
		while (cont < 10):
			adc_flag, adc_raw = bascula.leer_ADC()
			if(adc_flag == True):
				array_lecturaADC.append(adc_raw)
				punto_y2_2 = sum(array_lecturaADC[2:])/float(8)
				punto_y2 = punto_y2_2 -b
				cont = cont + 1
		punto_y1 = float(self.indicador_PesoConocido.get_text())
		self.i = -1
		m_posible = punto_y1/punto_y2
		self.button15.set_sensitive(True)
		print(m)
		return
	
	def delete (self, widget, button12):
		global flag_punto
		global posicion
		
		if(self.i <= -1):
			self.i = -1
		else:
			self.indicador_PesoConocido.delete_text(self.i, self.c)
			self.i = self.i-1
		if(self.i < posicion):
			self.button11.set_sensitive(True)
			self.button17.set_sensitive(True)
		if(self.i == -1):
			self.button17.set_sensitive(False)
		if(self.i == posicion):
			self.button17.set_sensitive(False)
			
		return
	
	def borrar_texto(self, widget, button13):
		self.indicador_PesoConocido.set_text("")
		self.button11.set_sensitive(True)
		self.i = -1
		self.button17.set_sensitive(False)
		return
		
	def reiniciar_calibracion(self, widget, button16):
		self.indicador_PesoConocido.set_text("")
		self.button15.set_sensitive(False)
		self.button17.set_sensitive(False)
		return
		
	def guardar_calibracion(self, widget, button15):
		global m_posible
		global m
		global punto_y1
		global punto_y2
		global b_posible
		global b
		m = m_posible
		b = b_posible
		m_texto = str(m_posible)
		file = open("Parámetros2.2.txt", "w")
		file.write(m_texto)
		b_texto = str(b_posible)
		file = open("Parámetros1.1.txt", "w")
		file.write(b_texto)
		self.window1.destroy()
		return
	
	def cancelar_calibracion(self, widgtet, button140):
		self.window1.destroy()
		return 

		
if __name__ == "__main__":
	
	file = open("Parámetros1.1.txt", "r")
	b = float((file.read()))
	file = open("Parámetros2.2.txt", "r")
	m  = float((file.read()))
	#b = 41300.0

	#m = 5.13000000000e-06 # 5.13125004581e-06
	print(b, m)

	serial_1 = True
	state1 = False
	state2 = False
	bascula.ini_ADC()
	leer_operador = leer_operador(args=())
	leer_operador.start()
	obtener_peso = obtener_peso(args=(), high=(), flag=())
	obtener_peso.start()
	ventana = ventana_principal(leer_operador, obtener_peso)
	gtk.timeout_add(200, ventana.updates)
	gtk.gdk.threads_init()                                           
	gtkt = threading.Thread(target=gtk.main, args=())          
	gtkt.start()



	
	
	
	
	

    
   
		
   
    

 
    
    

