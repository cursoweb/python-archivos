#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- ejercicio extra opcional.
Google's Python Class

Leer el archivo especificado en la línea de comandos.
Haz un split() simple en los espacios en blanco para 
obtener todas las palabras en el archivo.
En vez de leer el archivo línea por línea, es más fácil leerlo
en una cadena gigante y dividirlo 1 vez.

Construye un diccionario "mimic" que mapee cada palabra que 
aparece en el archivo a una lista de todas las palabras que siguen
inmediatamente a esa palabra en el archivo.
La lista de palabras puede estar en cualquier orden y debería
incluir duplicados. Así por ejemplo la llave "and" puede tener
la lista ["then", "best", "then", "after", ...] listando todas
las palabras que vienen después de "and" en el texto.
diremos que la cadena vacía es lo que viene antes de
la primer palabra en el archivo.

Con el diccionario mimic, es muy fácil emitir texto aleatorio
que imita al original. Imprime una palabra, y luego mira qué
palabras pueden venir luego y elige una al azar como la 
próxima palabra, y funcionará.
Utiliza una cadena vacía como la primer palabra para alivianar 
las cosas. Si nos quedamos trabados con una palabra que no está
en el diccionario, volvemos a la cadena vacía para que las 
cosas se muevan.

Nota: el módulo estandar de python 'random' incluye un método
random.choice(lista) que elige un elemento aleatorio de 
una lista no-vacía.

Para divertirnos, alimenta tu programa a sí mismo como entrada.
Puede funcionar mejor poner saltos de línea cada 70 columnas,
así la salida se ve mejor.

"""

import random
import sys


def mimic_dict(filename):
    """Retorna un diccionario mimic mapeando cada palabra a la lista de palabras que le siguen."""
    # +++tu código aquí+++
    return


def print_mimic(mimic_dict, word):
    """ Diccionario mimic dado y una palabra inicial, imprimir 200 palabras aleatorias."""
    # +++tu código aquí+++
    return


# main() provisto, llama a mimic_dict() y mimic()
def main():
    if len(sys.argv) != 2:
        print 'uso: ./mimic.py archivo-a-leer'
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
