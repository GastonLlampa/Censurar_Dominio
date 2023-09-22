import re
from Textos import *

texto_prueba = "Este es un ejemplo de una página web: https://proyectodalto.com y también podemos visitar http://example.org"

preUrl = re["www""https\:\/\/wwww"]

postUrl = re["com"]
 
patron_completo = "{preUrl}?+\.[a-zA-Z0-9.-]+\.{postUrl}"

resultado = re.findall(patron_completo, texto_prueba)

print(resultado)