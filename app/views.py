from django.http import HttpResponse
import urllib2
import json
import serial
try:
    conexion=serial.Serial("COM3",9600)
except:
    pass
def home(request):

    return HttpResponse("<style>h1{color:blue}</style><h1>Djangoduino</h1>")

def encender(request,estado):
    try:
        if estado=="1":
            conexion.write("1")
            return HttpResponse("<h1>Led encendido</h1><script>console.log(%s)</script>"%estado)

        elif estado>"1":
            return HttpResponse("<h1>En estos momentos no esta disponible</h1>")

        else:
            conexion.write("0")
            return HttpResponse("<h1>Led apagado</h1><script>console.log(%s)</script>"%estado)
    except:
        return HttpResponse("El Arduino no se encuentra conectado")
