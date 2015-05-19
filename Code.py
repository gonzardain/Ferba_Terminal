#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import pygtk
pygtk.require("2.0")


import gtk
import gtk.glade
import time
import datetime
import pango



class MainWin:
    
    def __init__(self):
        
        self.widgets = gtk.glade.XML("Principal.glade")
        
        
        signals = { 
                    "gtk_main_quit" : gtk.main_quit }
        
        
        self.widgets.signal_autoconnect(signals)
        self.label1 = self.widgets.get_widget("label1")
        
        self.button1 = self.widgets.get_widget("button1")
        self.button1.connect("clicked", self.clicked,  None)
               
        self.button2 = self.widgets.get_widget("button2")
        self.button2.connect("clicked", self.shutdown,  None)
        
        #self.button3 = self.widgets.get_widget("button3")
        #self.button3.connect("clicked", self.ChangeUser, None) 
        
        
  
    
    def push_item(self, data, prompt):
		try:
			context_id = self.statusbar.get_context_id("data")
			
			self.pop_item(context_id)
		except:
			pass
		self.statusbar.push(data, prompt)
		return
		
         
    def update(self):
        self.statusbar = self.widgets.get_widget("statusbar")
        context_id = self.statusbar.get_context_id("data")
        self.push_item(context_id, time.strftime('Configuración	               	        							               %d, %b %Y  --  %H:%M'))
        
        return True

    def clicked (self, widget, button1):
	
		dialog1 = KeyAdmin();
		run = dialog1.run()

    def shutdown (self, widget, button2):
		
		command = "/usr/bin/sudo shutdown -h now"
		import subprocess 
		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		output = process.communicate()[0]
		print output
		

    #def ChangeUser (self, widget, button3):
		#dialog3= IDOperator();
		#run = dialog3.run()
		
    
			
class KeyAdmin:
    def __init__(self, usuario="", Contrasena=""):
        
		self.gladefile = "Principal.glade"
		self.usuario= usuario
		self.Contrasena= Contrasena

    def run(self):

			  
		self.wTree = gtk.glade.XML(self.gladefile, "dialog1") 
		
		self.dlg = self.wTree.get_widget("dialog1")

		self.enuser = self.wTree.get_widget("enuser")
		self.enuser.set_text(self.usuario)
		self.enpassword = self.wTree.get_widget("enpassword")
		self.enpassword.set_text(self.Contrasena)
		self.result = self.dlg.run()
		self.usuario = self.enuser.get_text()
		self.Contrasena = self.enpassword.get_text()
		self.dlg.destroy()
		print ( self.usuario, self. Contrasena)
		
		
	
    
		if ( self.usuario== "a" and self.Contrasena== "a"):
			dialog2 = Menu();
			run = dialog2.run()
		else:
			dialog2 = Access_Denied();
			run = dialog2.run()	
	
class Menu:

    def __init__(self):
        
		self.gladefile = "Menu.glade"

    def run(self):
	  
		self.wTree = gtk.glade.XML(self.gladefile, "window1") 
		self.dlg = self.wTree.get_widget("window1")
		self.result = self.dlg.run()
		self.dlg.destroy()
		return 
	
class Access_Denied:
	
	def __init__(self):
		
		self.gladefile = "Contraseña.glade"
	
	def run (self):
		
		self.wTree = gtk.glade.XML(self.gladefile, "dialog2")
		self.dlg = self.wTree.get_widget("dialog2")
		self.result = self.dlg.run()
		self.dlg.destroy()
		return
		
class IDOperator:

	def __init__(self):
		
		self.gladefile = "Principal_8.glade"
	
	def run (self):
		
		self.wTree = gtk.glade.XML(self.gladefile, "dialog3")
		self.dlg = self.wTree.get_widget("dialog3")
		self.result = self.dlg.run()
		self.dlg.destroy()
		return

		
		    
def main():
    gtk.main()

if __name__ == "__main__":
    clock = MainWin()
    
    gtk.timeout_add(200, clock.update)
    
    main()
