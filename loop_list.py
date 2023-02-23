from urllib import *
import urllib.request
import json
url=input('Ingresa el bin --> : ')
sitio='https://lookup.binlist.net/'+url
respuesta=urllib.request.urlopen(sitio).read()

print(respuesta)
