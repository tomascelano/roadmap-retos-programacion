'''Operador de concatenacion de cadenas de caracteres 
 utilizando el operador de concatenacion + '''

hola = "Hola"
python = "Estoy programado en python"
saludo = hola + ' ' + python #inicializamos la variable Saludo alojando en ella la suma de 3 str
print(saludo) #imprimimos la variable tipo string saludo

'''Operadores logicos y booleanos'''
verdadero = True #variable booleana
falso = False #variable booleana

operador_logico_or = verdadero or falso #or = o
operador_logico_and = verdadero and falso #AND = y
operador_logico_not = not falso #NOT = inversor

print("---Operadores logicos")

print("resultado verdadero or falso")
print(operador_logico_or)
print("resultado erdadero and falso")
print(operador_logico_and)
print("resultado not falso")
print(operador_logico_not)

operador_logico_not = not verdadero 

print("resultado not verdadero")
print(operador_logico_not)

verdadero = 1
falso = 0

operador_logico_or = verdadero or falso 
operador_logico_and = verdadero and falso 
operador_logico_not = not falso 

print("resultado 1 or 0 ")
print(operador_logico_or)
print("resultado 1 and 0 ")
print(operador_logico_and)
print("resultado not 0")
print(operador_logico_not)

operador_logico_not = not verdadero 

print("resultado not 1")
print(operador_logico_not)

'''Operadores de comparacion
'''

print("---Operadores de comparacion")
uno = 1
cero = 0

mayor = uno > cero
menor = uno < cero
igual = uno == cero
distinto = uno != cero

print("Uno mayor que cero?")
print(mayor)
print("Uno menor que cero?")
print(menor)
print("Uno igual a cero?")
print(igual)
print("Uno distinto a cero?")
print(distinto)

'''Operadores aritmeticos'''
print("---Uso de operadores aritmeticos---")

print(f"Suma: 10 + 8 = {10 + 8}")
print(f"Resta: 10 - 8 = {10 - 8}")
print(f"Multiplicacion: 10 * 8 = {10 * 8}")
print(f"Division: 10 / 8 = {10 / 8}") #Obtiene el resultado de dividir el operando de la izquierda por el de la derecha. El resultado siempre es float
print(f"Modulo: 10 % 8 = {10 % 8}") #Obtiene el resto de dividir el operando de la izquierda por el de la derecha
print(f"Cociente entero: 10 // 8 = {10 // 8}")#Se obtiene el cociente entero de dividir el operando de la izquierda por el de la derecha
print(f"Potencia: 10 ** 8 = {10 ** 8}")#El resultado es el operando de la izquierda elevado a la potencia del operando de la derecha

'''
Operadores a nivel de bits 
'''

print("---Uso de operadores a nivel de bits---")
print(f"Logica AND entre binario 101 y 011 que en decimal son 5 y 3 resultado {5 & 3}")
print(f"Logica OR entre binario 101 y 011 que en decimal son 5 y 3 resultado  {5 | 3}")
print(f"Logica XOR entre binario 101 y 011 que en decimal son 5 y 3 resultado {5 ^ 3}")#Al comparar cada bit si los bits son diferentes el resultado es uno si son iguales el resultado es uno
print(f"NOT binario 101 en decimal es 5 resultado  { ~ 5}")#Este operador invierte todos los bits del numero. En Python, los números enteros son representados en complemento a dos
print(f"Dezplazamiento a la izquierda de 2 bit del binario 101 {5 << 2}")#Este operador desplaza los bits de un número a la izquierda. #
print(f"Dezplazamiento a la derecha de 2 bit a la derecha del binario 101 {5 >> 2}")#Este operador desplaza los bits de un número a la derecha. 

'''
Operadores de asignacion
'''

print("---Operadores de asignacion")
mi_numero = 3
print(mi_numero)
mi_numero += 1 #suma y asignacion
print(mi_numero)
mi_numero -= 2 #resta y asignacion
print(mi_numero)
mi_numero *= 6 #multiplicacion y asignacion
print(mi_numero)
mi_numero /= 4 #division y asignacion
print(mi_numero)
mi_numero %= 8 #Modulo y asignacion
print(mi_numero)
mi_numero //= 2 #Division entero y asignacion
print(mi_numero)
mi_numero **= 4 #Potencia y asignacion
print(mi_numero)

'''
Operadores de identidad
'''

print("---Operadores de identidad")
mi_nuevo_numero = mi_numero

print(f"mi_numero is mi_nuevo_numero es {mi_numero is mi_nuevo_numero}")#Devuelve True si ambos operandos hacen referencia al mismo objeto, es decir, si tienen la misma dirección en memoria.
print(f"mi_numero is not mi_nuevo_numero es {mi_numero is not mi_nuevo_numero}")#Devuelve True si ambos operandos no hacen referencia al mismo objeto


'''
Operadores de pertenencia
'''
print("---Operadores de pertenencia")
print(f" 'o' in 'tomi' = {'o' in 'tomi'}")
print(f" 'c' not in 'tomi' = {'c' not in 'tomi'}")

lista = [1, 4, 7]
print(f"Mi lista es {lista}")
print
print(f"Mi lista tiene el numero 2? {2 in lista}")
print(f"Mi lista tiene el numero 4? {4 in lista}")
print(f"Mi lista no tiene el numero 2? {2 not in lista}")

'''
Estructuras de control
'''

#Condicionales
print("Estructuras de control condicionales if-elif-else")
mi_string = "Tomass"
if mi_string == "Tomas": #if = si algo se cumple haz algo si no se cumple haz otra cosa
    print("mi_string es 'Tomas'")
elif mi_string == "Toms": #condicion2
    print("mi_string es 'Toms'")
elif mi_string == "Tomass": #condicion3
    print("mi_string es 'Tomass'")
else: #si ninguna condicion es verdadera haz esto
    print("mi_string no es 'Tomass'")

#iterativas
print("Estructuras de control iterativas")
for i in range(21): #for es una estructura iterativa nos sirve para recorrer estructuras que tienen mas de un elemeto o ejecutar una acccion varias veces
    print(i)

while i <= 30: #el bucle se ejecuta mientras la condicion es verdadera    
    print(i)
    i += 1

#Manejo de excepciones
print("Estructuras de control manejo de excepciones")
try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

print("Ejercicio")
#Ejercicio
for numero in range(10,56): #hacemos que la variable numero recorra desde el 10 hasta el 55
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0: #Es par si se cumple que el numero divido entre dos da resultado resto cero, si es distinto de 16 y si divido entre 3 da resultado distinto de 0 se cumple la condicion
        print(numero)
