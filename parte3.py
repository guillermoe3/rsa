import math
import string


def textToNum(texto_toarr, max_exp, n):
        acum=0
        cont=0
        base=26
        for j in texto_toarr:
            
            #Si N < al texto cifrado devuelvo -1
            #max_exp =max_exp-1
            if (max_exp < 0):
                return -1
            if ((int(string.ascii_lowercase.index(j))*(base**(max_exp)))>n):
                max_exp=max_exp-1
            cont = (int(string.ascii_lowercase.index(j))*(base**(max_exp)))
            #print("{3} = Queda el num {0} por {1} pow {2}".format((int(string.ascii_lowercase.index(j))), base, max_exp, j))
            acum=acum+cont
            cont=0
            max_exp =max_exp-1
        return acum

def numToText(num, max_exp):
    base26 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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

#ejemplo d= 26767
#ejemplo n=46927

def mensajeDesenc(texto_toarr, max_exp, n):
    
    numCifrado = textToNum(texto_toarr,max_exp, n)
    numPlano = (numCifrado**d)%n

    textoPlano = numToText(numPlano,max_exp)
    return textoPlano

print("Ingrese la clave de descifrado {d,n}")
d =int(input("Ingrese d: "))#26767#
n =int(input("Ingrese n: "))#46927#

print("La clave de des-encriptación ingresada es D={0}, N={1}".format(d,n) )
#La clave privada consiste de { d,n } y la clave pública consiste de {e,n }
base = 26
max_exp = int(math.log(n, base))

print("El exponente maximo es:",max_exp)

texto="tienemasde5"
while(len(texto) >5 ):
    texto = input("Ingrese un texto de hasta 5 letras:")
texto_toarr = list(texto)

#Valdio si N < descifrado de texto_toarr. Si es menor, pedir otro texto u otra N mayor.

if (textToNum(texto_toarr,max_exp,n) != -1):
    #print(texto_toarr)
    print("El texto plano es: ",mensajeDesenc(texto_toarr,max_exp, n))
else: 
    print("N es menos al numero cifrado. Pruebe con otro N o Texto Cifrado que no supere a N")

#print("El texto plano es: ",mensajeDesenc(texto_toarr,max_exp))
