#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import sys
import numpy


GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.IN)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(06, GPIO.IN)

tiempo = .001


def Cal(self, device = "peso"):
	x = CLCK(object)
	peso = float((x*113))
	peso1 = ((peso/26606) - 130 ) / 1000
	return (peso1)
	
def CLCK(self, device = "adc"):
	
	adc = int(0)
	x = 24
	
	for i in range (0, x):
		GPIO.output(19, True)
		time.sleep(tiempo)
		GPIO.output(19, False)
		adc |= GPIO.input(26)
		adc <<= 1
		time.sleep(tiempo)
	
	GPIO.output(19, True)
	time.sleep(tiempo)
	GPIO.output(19, False)
	
	if((adc >> 23 & 1) == 1):
		
		adc = (adc - 33554432) # no se que hizo ivan aqui preguntar
		
	return adc
	
def main():
        

        GPIO.output(19, False)
        GPIO.output(13, False)

        while (GPIO.input(06) == False):
			

            a = GPIO.input(26)
            
            if (a == 0):
			    time.sleep(tiempo)
			    
			    b = Cal(object)
			    print float("%.2f" % b)
			 
            else:
				GPIO.output(19, False)
				 
	

if __name__ == '__main__':

       main()
       






