import re

#def reWrite():

print("Ingrese url a eliminar")
url_delete = input()
patron1 = 'www\.'+url_delete+'\.[a-z]{2,3}'
patron2 = 'https:\/\/www\.'+url_delete+'\.[a-z]{2,3}'
patron3 = 'https:\/\/'+url_delete+'\.[a-z]{2,3}'
patron4 = 'http:\/\/www\.'+url_delete+'\.[a-z]{2,3}'
patron5 = 'http:\/\/'+url_delete+'\.[a-z]{2,3}'
patron6 = url_delete+'\.[a-z]{2,3}'
patron_completo = patron1+'|'+patron2+'|'+patron3+'|'+patron4+'|'+patron5+'|'+patron6

texto = open('texto_1.txt', 'r')
lineas = texto.read()

#resultado = re.search(patron_completo, item, flags=re.IGNORECASE)
print("Archivo Inicial")
print(lineas)
lineas=re.sub(patron_completo, '-', lineas, flags=re.IGNORECASE)
print("Archivo resultante")
print(lineas)
print("Desea reescribir el archivo? Si | NO")
op = input()
if (op.lower() == 'si'):
    archivo = open('texto_1.txt', 'w')
    archivo.write(lineas)
    archivo.close()
    print("Archivo Reescrito")
texto.close()