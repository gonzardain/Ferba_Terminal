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
ADC_running=False
UART_running=False
ADC_pause=False

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
########################################################################################################################
    # Funcion updates incluye las tareas que se hacen recurrentes como
    # leer el pin si se ha desconectado
    # preguntar si hay un peso maximo
    # actualizar la hora del reloj
    # lee si hay un operador nuevo
########################################################################################################################
    def updates(self):
		global ADC_running
		global UART_running
		if(GPIO.input(18) ==1):
			command = "/usr/bin/sudo shutdown -h now"
			import subprocess
			process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
			output = process.communicate()[0]
			print output
		else:
			try:
				self.statusbar1 = self.widgets.get_widget("statusbar1")
				context_id = self.statusbar1.get_context_id("data")
				self.escribir_estado(context_id, time.strftime('                	               	                             %d, %b %Y  --  %H:%M'))

				self.etiqueta_IDoperator.set_text(leer_operador.args)
				self.indicador_PesoActual.set_text(obtener_peso.args)
				self.indicador_Peso.set_text(obtener_peso.high)
				if(obtener_peso.flag == True):
					self.indicador_FechaHora.set_text(time.strftime('%d, %b %Y  --  %H:%M'))
			except:	
				ADC_running=False
				UART_running=False
				gtk.main_quit()
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
########################################################################################################################
    # Clase que lee la tarjeta de RFid del operador
########################################################################################################################
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
		global UART_running
		#ser = serial.Serial ("/dev/ttyAMA0")
		

		while (UART_running):
			ser = serial.Serial ("/dev/ttyAMA0")
			ser.baudrate = 9600
			#a = ser.read(13)
			a=''
			ser.flush()
			ser.close()
			self.args = a
			
			
			time.sleep(0.1)#
		
		
		return 0
########################################################################################################################
    # Clase que lee el valor del peso filtrado del script bascula.py y lo muestra en la funcion updates
########################################################################################################################	
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
		global n
		global m
		global ADC_running
		global ADC_pause
		limh = 2
		max1 = limh
		flaglim = 0
		cont = 0
		parametros_filtro = bascula.ini_filtrar_ADC()
		print (ADC_running)
		while(ADC_running==True):
			if (ADC_pause == False):
				#print('ADC still running')
				self.flag = False
				limh = float(2.0)
				adc_flag, adc_raw = bascula.leer_ADC()
				
				if(adc_flag == True):
					peso_escalado = bascula.escalar_Peso(m, n, adc_raw) # 22073.0
					#valor_peso_indicador = peso
					#print(adc_raw)
					valor_peso_indicador,parametros_filtro=bascula.filtrar_ADC(parametros_filtro, peso_escalado)
					if (valor_peso_indicador > max1 and flaglim == 1):
						max1 = valor_peso_indicador
					if (valor_peso_indicador <= limh and flaglim == 1):
						self.flag = True
						max1_texto = str(max1)
						self.high = max1_texto[:3]
						flaglim = 0
						max1 = limh
						time.sleep(1)
					
					if (valor_peso_indicador >= limh and flaglim == 0):
						flaglim = 1
					if (valor_peso_indicador < 0):
						valor_peso_indicador=0
					valor_peso_indicador_txt = str("%0.2f" %valor_peso_indicador)
					self.args = valor_peso_indicador_txt
			else:
				time.sleep(1)
				#return
				#print('ADC paused')	

########################################################################################################################
    # Clase que abre la opcion del menu
########################################################################################################################

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
########################################################################################################################
    # Clase que abre la opcion de calibracion de la bascula y hace la funcion de calibracion
########################################################################################################################
class operation():
	global b
	global m
	
	def __init__(self):
		global ADC_pause
		ADC_pause=True
		
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
		global punto_y1
		array_lecturaADC = []
		cont = 0
		while (cont < 10):
			adc_flag, adc_raw = bascula.leer_ADC()
			if(adc_flag == True):
				array_lecturaADC.append(adc_raw)
				punto_y1 = sum(array_lecturaADC[2:])/float(8)
				cont = cont + 1
		punto_y1 
		print(array_lecturaADC[2:])
		return

	def obtener_punto2 (self, widget, button17):
		global punto_x2
		global punto_y2
		array_lecturaADC = []
		cont = 0
		while (cont < 10):
			adc_flag, adc_raw = bascula.leer_ADC()
			if(adc_flag == True):
				array_lecturaADC.append(adc_raw)
				punto_y2 = sum(array_lecturaADC[2:])/float(8)
				cont = cont + 1
		punto_x2 = float(self.indicador_PesoConocido.get_text())
		self.i = -1
		self.button15.set_sensitive(True)
		print(array_lecturaADC[2:])
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
		global punto_x1
		global punto_y1
		global punto_x2
		global punto_y2
		global ADC_pause
		global m
		global n
		punto_x1 = 0
		print  punto_x1, punto_x2, punto_y1, punto_y2
		m = 1/((punto_y2 - punto_y1)/(punto_x2))
		n = punto_y1
		print m, n
		m_texto = str(m)
		file = open("Parámetros2.2.txt", "w")
		file.write(m_texto)
		n_texto = str(n)
		file = open("Parámetros1.1.txt", "w")
		file.write(n_texto)
		ADC_pause = False
		self.window1.destroy()
		return
	
	def cancelar_calibracion(self, widgtet, button140):
		global ADC_pause
		ADC_pause = False
		self.window1.destroy()
		return 

		
if __name__ == "__main__":
	global punto_x1
	global punto_y1
	global punto_x2
	global punto_y2
	global m
	global n
	
	
	ADC_running=True
	UART_running=True
	file = open("Parámetros1.1.txt", "r")
	n = float((file.read()))
	file = open("Parámetros2.2.txt", "r")
	m  = float((file.read()))
	#n = 41300.0

	#m = 5.13000000000e-06 # 5.13125004581e-06
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
	time.sleep(1)        
	gtkt.start()


	
	
	
	
	

    
   
		
   
    

 
    
    

