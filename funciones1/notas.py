import json 
def notas(): 
    notas1=int(input('Ingrese la nota 1: '))
    notas2=int(input('Ingrese la nota 2: '))
    nota=(notas1+notas2)/2
    if nota>60:
        pass
    with open("funciones1/camper.json","r") as file:
            inscritos = json.load(file)
notas()
    






        
