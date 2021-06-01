import string
import math
from typing import List
import numpy

base26 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#region "Funciones"

def numToString(num, max_exp):
    palabra = ""
    m=-1
    acum=num
    for exp in range(max_exp,m,-1):

        m2 = 0
        for alp in range(26, m2, -1):

           temp = int(acum/(alp*(26**exp)))
           if (temp >0  ):

               acum = acum - (alp*(26**exp))

               palabra = palabra + base26[alp]
                
    return palabra

def dividirArray(alist, partes=1):
    length = len(alist)
    return [ alist[i*length // partes: (i+1)*length // partes] 
             for i in range(partes) ]

def arrayDeArray(texto_toarr, max_exp):
    acum=0
    cont=0
    for i in texto_toarr:
        # print("Esto es IIIIIIII--------------------------------------------------------", i)
        temp_max=max_exp
        for j in i:
            
            #print("Esto es JJJJJJJJJJJJJJJJJJJJJJJJJJJ:", j)
            #print(string.ascii_lowercase.index(j))
            #valornum= int(string.ascii_lowercase.index(i))
            temp_max =temp_max-1
           # print("Exponente",temp_max)
            if (temp_max < 0):
                print("EL EXPONENTE LLEGO A CERO. Ingrese un N mas grande o un texto mas corto")
                #break
            cont = (int(string.ascii_lowercase.index(j))*(base**(temp_max)))
            print("ESTE ES EL CONTADOR ", cont)
            print("Esto es la base a la MaxExp potencia",(base**(temp_max)))
            

            acum=acum+cont
            #print(cont)
            cont=0
    print("Esto es el acumulador: ",acum)
    return acum

def arraySolo(texto_toarr, max_exp):
        acum=0
        cont=0
        for j in texto_toarr:
            
            max_exp =max_exp-1
            if (max_exp < 0):
                print("EL EXPONENTE LLEGO A CERO. Ingrese un N mas grande o un texto mas corto")
                    #break
            cont = (int(string.ascii_lowercase.index(j))*(base**(max_exp)))
            acum=acum+cont
            cont=0
        return acum

def concat(arraytemp):
    texto = ""
    for i in arraytemp:
        texto = texto +i
    return texto
#endregion

print("Ingrese la clave de encriptación {e,n}")
e = int(input("Ingrese e: "))
n = int(input("Ingrese n: "))


#Compruebo que la clave corresponda con la cantidad de caracteres del texto:
base = 26
max_exp = int(math.log(n, base))
#print("El exponente maximo es:",max_exp)


#print("Ingrese un texto de hasta 5 letras que no contengan la letra A. \nEn base al N ingresado, se sugiere utilizar un texto no mayor a {0} caracteres para reutilizarlo en la parte 3".format(max_exp))

print("\nIngrese un texto tal que: ")
print("     - No tengan la letra A.\n     - No tengan más de 5 letras")
print("     - Para reutilizar estos valores en la parte 3, se sugiere utilizar un texto no mayor a {0} caracteres (por el N ingresado)\n".format(max_exp))
texto="tienemasde5"
while(len(texto) >5 ):
    texto = input("Ingrese un texto de hasta 5 letras: ")
texto_toarr = list(texto)

print("La clave de encriptación ingresada es E={0}, N={1}".format(e,n) )
print("El texto se dividió de la siguiente forma: ",texto_toarr)


#recorro el texto
acum = 0
cont = 0

if (len(texto_toarr) > max_exp):
    div = math.ceil(len(texto_toarr)/max_exp)
    print("El texto se dividirá en bloques de: ", div)
    texto_toarr = dividirArray(texto_toarr,div)
    #print("Este es el array de arrays:", texto_toarr)
    arrayTemp = []
    for i in texto_toarr:
        acum = arraySolo(i,max_exp)
        arrayTemp.append(acum)
    try:
        
        cifradoText = []
        print("El texto cifrado en numero es: ", (arrayTemp))
        for i in arrayTemp:
            numCifrado = int((i**e)% n)
            temp = (numToString(numCifrado,max_exp))
           # print("Esto es el texto cifrado:", temp)
            cifradoText.append(temp)
        print("El texto cifrado es (como array): ", cifradoText)
        print("El texto cifrado es (en string)", concat(cifradoText))
    except OverflowError as err:
        print("La clave no matchea con el texto ingresado.", err)

else:
    acum = arraySolo(texto_toarr,max_exp)
    try:
        cifrado = int((acum**e)% n)
        print("El texto cifrado en numeros es: ", (cifrado))
        print("El texto cifrado es: ",numToString(cifrado, max_exp))
    except OverflowError as err:
        print("La clave no matchea con el texto ingresado.", err)


