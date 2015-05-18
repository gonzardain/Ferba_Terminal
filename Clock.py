#!/usr/bin/env python
# -*- coding: utf-8  -*-

import pygtk
pygtk.require('2.0')
import gtk
import time

class Clock:

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_title("Clock")
        self.label = gtk.Label()
        window.add(self.label)
        window.set_border_width(25)
        window.show_all ()

    def update(self):
        self.label.set_text(time.strftime('%H:%M:%S'))
        return True  #needed to keep the update method in the schedule

def main():
    gtk.main()

if __name__ == "__main__":
    clock = Clock()
    gtk.timeout_add(200, clock.update)  #add to the main loop scheduled tasks
    main()
