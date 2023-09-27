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
lineas = texto.readlines()
for item in lineas:
    #resultado = re.findall(patron_completo, item)
    resultado = re.search(patron_completo, item)
    star_url = resultado.start()
    fin_url = resultado.end()
    i = 0
    lista = list(item)
    for caracter in lista:
        if(star_url <= i & i < fin_url):
            lista[i] = '-'
        i = i + 1
    item = ''.join(lista)
    print(item)
    #texto.write(item)
    print(resultado)
    #reWrite()

texto.close()