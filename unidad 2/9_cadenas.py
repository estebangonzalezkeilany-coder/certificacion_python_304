#cadenas y concatenacion con (+)
cadena1="hola"
cadena2="mundo"
multilinea="""esto es una cadena
de varias lineas"""
print(cadena1+cadena2)#print()
#cadenas y repeticion
eco="ja"*3
print(eco)
#cambia una cadena de minuscula a mayuscula
tu_nombre="keilani"
print(tu_nombre.upper())
#cambia una cadena de mayuscula a minuscula
print(tu_nombre.lower())
#reemplaza texto en una cadena
frase="me gusta programacion"
print(frase.replace("programacion","matematicas"))
#formato de cadenas(f-string)
edad=17
nombre="luis"
mensaje=f"hola me llamo\n{nombre}\ny tengo\n{edad}años"
print(mensaje)
#contar los caracteres de una cadena
texto="!felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra
oracion="aprender python es divertido"
if "python" in oracion:
    print("encontrado")
else:
 print("no esta")
#validar contenido de una cadena
nlista=13
print(nlista.isalpha())
print(nlista,isdijit())