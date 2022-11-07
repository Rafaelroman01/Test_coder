from django.http import HttpResponse
from django.template import Template, Context

from datetime import datetime
import os

def fecha_actual(request):
    hoy = datetime.now().strftime("%Y|%m|%d")
    return HttpResponse(hoy)

def inicio(request):
    
    path_actual = os.path.basename(".")
    print(path_actual)
    # Leemos el contenido del archivo HTML
    archivo = open("C:/Users/Familia/Documents/CODER44470/ac_django/test_coder/test_coder/templates/inicio.html")
    
    # Creamos una plantilla a partir del contenido del archivo plantilla
    plantilla = Template(archivo.read())
       
    # Cerramos el archivo porque no lo usamos mas
    archivo.close
       
    #Creamos el contexto que necesita la plantilla
       
    contexto = Context()
    # Generar el documento a devolver al usuario
       
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
