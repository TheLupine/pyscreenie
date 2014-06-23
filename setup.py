#!/usr/bin/env python

from distutils.core import setup
import os, sys
import glob


glade_files = glob.glob("glade/*")    
setup(name = "pyscreenie",
    version = "1.9.4",
    description = "Python/Glade/GTK app to grab a timed screenshot",
    author = "Lupine",
    author_email = "lupine@thelupine.com",
    url = "http://www.thelupine.com/pyscreenie",
    license = "GPL 2",
    data_files=[('/usr/share/pyscreenie/', glade_files), 
                ('/usr/share/man/man1', ['pyscreenie.1.gz'])],
                ('/usr/share/applications', ['pyscreenie.desktop'])],
    scripts=["src/pyscreenie","src/pyscreenie-scheduler"],
    long_description = """pyscreenie is a simple Python/Glade/GTK application that presents the user \
with a simple set of choices that will allow them to setup a schedule to take a screenshot of the \
main desktop.""")
      
