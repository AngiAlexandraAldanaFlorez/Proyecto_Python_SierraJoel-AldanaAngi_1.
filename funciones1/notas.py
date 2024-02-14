import json
import notas
from mua import lista_campers

with open("camper.json") as file:
        inscritos = json.load(file)


#Notas de ingreso
notas=int(input('Ingrese la nota 1'))
notas2=int(input('Ingrese la nota 2'))

nota=(notas+notas2)/2

if nota>60:
    if lista_campers["Estado"].lower() == "aprobado":
        inscritos["campus"]["aprobado"].append(lista_campers)
    
