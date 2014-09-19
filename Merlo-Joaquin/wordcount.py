#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

La función main() de abajo ya está definida y completa. Llama a las funciones
print_words() y print_top() que escribiste.

1. Para la bandera --count, implementar una función print_words(nombre_archivo) que cuenta
qué tan frecuentemente cada palabra aparece en el texto e imprime:
palabra1 cantidad1
palabra2 cantidad2
...

Imprimir la lista de arriba ordenadas por palabras (python ordenará para que la puntuación 
venga antes de las letras -- no se preocupen por eso). Guardar todas las palabras en minúsculas,
así 'The' y 'the' cuentan como la misma palabra.

2. para la bandera --topcount, implementar una función print_top(nombre_archivo) que es 
similar a print_words() pero imprime sólo las 20 palabras más comunes ordenadas
para que aparezca la palabra más común primero, luego la siguiente más común, y así.

Utilizar str.split() (sin argumentos) para dividir todo por los espacios en blanco.

Flujo de trabajo: no construyas todo el programa de una vez. Llega hasta un hito intermedio 
e imprime tu estructura de datos y luego sys.exit(0).
Cuando eso funcione, intenta con el siguiente hito.

Opcional: defina una función de ayuda para evitar duplicar código dentro de 
print_words() y print_top().

"""

import sys

# +++tu código aquí+++
# Define las funciones print_words(nombre_archivo) y print_top(nombre_archivo).
# Puedes escribir una función de ayuda que lee un archivo y construye y retorna
# un diccionario palabra/cantidad.
# Luego print_words() y print_top() pueden llamar directamente a la función de ayuda.
def print_words(namefile):
    f = open(namefile,'rU')
    diccionario={}
    contador = 1
    for linea in f:
        palabras = linea.split()
        for cadena in palabras:
            if not diccionario.has_key(cadena):
                diccionario[cadena]= contador
            else: 
                diccionario[cadena]= diccionario.get(cadena)+1
    f.close()
    return diccionario

def print_top(namefile):
    pass

    return
###

# Se provee este código básico de parseado de argumentos de línea de comandos
# que llama a las funciones print_words() y print_top() que debes definir.
def main():
    if len(sys.argv) != 3:
        print 'uso: ./wordcount.py {--count | --topcount} archivo'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'opcion desconocida: ' + option
        sys.exit(1)

if __name__ == '__main__':
    main()
