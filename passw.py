#!/usr/bin/python
#-*- coding:utf-8 -*-

fd=open("/etc/passwd","r")
lineas=fd.readlines()

dicc={}

for linea in lineas:
    conf = linea.split(":")
    username = conf[0]
    shell = conf[-1][:-1]
    dicc [username] = shell
    
try:
	print "root", dicc["root"]
	print "imaginario", dicc["imaginario"]
except:
	print "El usuario no existe"

    
