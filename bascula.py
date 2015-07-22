#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Báscula.py
#  
#  Copyright 2015  <pi@raspberrypi>
#  
#  

import time
import RPi.GPIO as GPIO
import sys
import scales_W_P
global b
global m


tiempo = .001								# Variable Global

def ini_ADC():
	GPIO.setmode(GPIO.BCM)					# Habilitar los pines de GPIO
	GPIO.setup(19, GPIO.OUT)				# SCLK_ADC conectado al pin 19 es salida
	GPIO.setup(26, GPIO.IN)					# Data-OUT_ADC conectado al pin 26 es entrada
	GPIO.setup(13, GPIO.OUT)				# Speed_ADC conectado al pin 13 es salida
	GPIO.output(19, False)					# Inicializar SCLK_ADC con 0
	GPIO.output(13, False)					# Inicializar Speed_ADC con 0
 
def leer_ADC():
	adc = int(0)							# inicializar adc con 0
	rango = 24        						# Determinar el rango para que haga 24 pulsos
	data_out_adc = GPIO.input(26)
	if (data_out_adc == 0):
		time.sleep(tiempo)
		for i in range (0, rango):			# inicia ciclo de 24 pulsos
			GPIO.output(19, True)		    # SCLK_ADC en alto
			time.sleep(tiempo)			    # Espero un tiempo
			GPIO.output(19, False)          # SCLK_ADC en bajo
			adc |= GPIO.input(26)		    # ADC OR Data-OUT_ADC
			adc <<= 1                       # Desplaza el valor de adc un lugar a la izq
			time.sleep(tiempo)				# Espero un tiempo
		GPIO.output(19, True)               # SCLK_ADC en alto
		time.sleep(tiempo)					# Espero un tiempo
		GPIO.output(19, False)				# SCLK_ADC en alto
	
		if((adc >> 23 & 1) == 1):			# Condición para leer negativos
			adc = (adc - 33554432)
		#print adc
		return  True, adc 
	
	else:
		GPIO.output(19, False)
	
		return False, 0 
		
def escalar_Peso(m, b, adc):
	primera_iteracion = adc - b
	peso = primera_iteracion * m
	New_adc_data = peso
	#print peso
	#print (m, b, adc)

	return New_adc_data
	
def ini_filtrar_ADC():
	moving_array=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	array_sorted = moving_array
	array_size = len(moving_array)
	new_data_threshold = 10
	display_threshold = 0.005
	Previous_adc_data = 0
	Display_previous_value = 0
	i = 0
	a = 0 
	media = 0.0
	
	Filter_data={'moving_array': moving_array, 'array_sorted': moving_array,'array_size':array_size,'new_data_threshold':new_data_threshold, 'display_threshold':display_threshold, 'Previous_adc_data':Previous_adc_data, 'Display_previous_value':Display_previous_value,'i':i,'media':media }

	
	return Filter_data
	
def filtrar_ADC(Parametros_filtro, peso_escalado):
	New_adc_data = peso_escalado

	
	if Parametros_filtro['new_data_threshold'] > abs(New_adc_data - Parametros_filtro['media']):
		Parametros_filtro['moving_array'][Parametros_filtro['i']]=New_adc_data
		Parametros_filtro['array_sorted'] = sorted(Parametros_filtro['moving_array'])[1:Parametros_filtro['array_size']-1]
		Parametros_filtro['media']=(sum(Parametros_filtro['array_sorted']))/(Parametros_filtro['array_size']-2)
		Parametros_filtro['i'] = Parametros_filtro['i']+1
	elif Parametros_filtro['new_data_threshold'] < abs(New_adc_data-Parametros_filtro['Previous_adc_data']):
		Parametros_filtro['Previous_adc_data'] = New_adc_data
		for j in range(Parametros_filtro['array_size']):
			Parametros_filtro['moving_array'][j]=New_adc_data
			Parametros_filtro['media'] = New_adc_data
			Parametros_filtro['i'] = 0
	if Parametros_filtro['i'] == 7:
		Parametros_filtro['i'] = 0
		print(Parametros_filtro['media'])
	Display_actual_vaue = Parametros_filtro['media'] 
	if Parametros_filtro['display_threshold'] <= abs(Display_actual_vaue-Parametros_filtro['Display_previous_value']):
		print(Display_actual_vaue)
		Parametros_filtro['Display_previous_value'] = Display_actual_vaue
	return Display_actual_vaue
			
		
				
		


if __name__ == "__main__":
	m = 5.13000000000e-06  
	b = 41300.0
	iniADC = ini_ADC()
	iniFiltro = ini_filtrar_ADC()
	while True:
		flag, adc = leer_ADC()
		if(flag == True):
			
			PesoEscalado = escalar_Peso(m, b, adc)
			filtrarADC = filtrar_ADC(iniFiltro, PesoEscalado)
			#iniFiltro = filtrarADC
		
	
	

