#!/bin/bash


ruta=$(pwd)

if [ -e $ruta/interface.py ];then
	python3 interface.py
else
	echo "Ocurrio un error en la instalacion"
fi
