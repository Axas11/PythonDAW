#Ejercicio 6. Crea un programa que lea tres variables: inicio, fin y nVeces. Pudiendo ser inicio y fin números reales. El programa deberá crear <nVeces> números reales aleatorios entre <inicio> y <fin> redondeados a dos cifras decimales. 
import random

inicio = 0
fin = 0
nVeces = 0
numero = 0

def datos():
    inicio = float(input("Inicio: "))
    fin = float(input("Fin: "))
    nVeces = int(input("Cantidad de números: "))
    return inicio, fin, nVeces

inicio, fin, nVeces = datos()

for _ in range(nVeces):
    numero = round(random.randint(inicio, fin), 2)
    print(numero)
