from django.http import HttpResponse
import urllib2
import json
import serial
conexion=serial.Serial("COM3",9600)
def home(request):

    if conexion.isOpen():
        return HttpResponse("Lacomunicacion se ha establecido")
    else:
        return HttpResponse("No hay conexion")

def encender(request,estado):
    if estado=="1":
        conexion.write("1")
        return HttpResponse("<h1>Led encendido</h1><script>console.log(%s)</script>"%estado)

    elif estado>"1":
        return HttpResponse("<h1>En estos momentos no esta disponible</h1>")

    else:
        conexion.write("0")
        return HttpResponse("<h1>Led apagado</h1><script>console.log(%s)</script>"%estado)
