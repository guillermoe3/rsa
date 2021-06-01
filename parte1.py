import secrets
import math


#region "Funciones"
    
def calculoD(e,o):

    d = secrets.SystemRandom().randrange(2,o)
    while (1):
        if (((d*e)%o) != 1):
            d = secrets.SystemRandom().randrange(2,o)
            
        else: return d

def mcd(a, b):
    temp = 0
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

#endregion

#Elijo PyQ
#1. Elegir dos números primos p y q ( p=7 y q=17)
print("Elija dos numeros primos P y Q entre 1 y 100")
print("Ejemplos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97")

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 977, 821, 157, 271]

p=1
while p not in primos:
    p=int(input("Numero primo P: "))
q=1
while q not in primos:
    q=int(input("Numero primo Q: "))

#print("El valor de P es este: ",p," y el valor de Q es: ",q)

#2. Calcular n= p.q ( m= p.q = 7x17 = 119
n=p*q;
print("El valor de N es: ",n)

#3. Calcular ø = (p-1)(q-1) ( ø = 96 ).
o=(p-1)*(q-1)
print("El valor de O es: ",o)

#4. Elegir un e que sea primo relativo de ø ( e = 5 )
#Calculo maximo comun divisor. 

#Elijo un numero aleatorio
e = secrets.SystemRandom().randrange(1,o)

#encuentro e que sea primo relativo de o. 
resul = math.gcd(e,o)
while resul != 1:
    e = secrets.SystemRandom().randrange(2,o)
    resul = math.gcd(e,o)
    #print(e)

#5. Determinar d tal que 1 = d.e mod 96 ( d = 77 )
#e.d - 1 = mod phi
  
#6. Muestro las claves generadas. 
#E Publica. 
#D Privada. 
d= calculoD(e,o)

print("La clave pública es el valor de E: ",e)
if (d == e):
    d= calculoD(e,o)
print("La clave privada es el valor de D: ",d)

##Realizo el cifrado y descifrado

m=int(input("Ingrese numero para probar el cifrado: "))
cifrado = m**e % n

#print(pow(m,e)%n)
print("El numero cifrado es: ", cifrado)

#para descifrar: 
descifrado= pow(cifrado,d) % n
descifrado2 = (m**(e*d)) % n
print("Este es el numero descifrado: ",descifrado)

