from notas import options

import json 
def notes(): 
    options()
    notas1=int(input('Ingrese la nota 1: '))
    notas2=int(input('Ingrese la nota 2: '))
    nota=(notas1+notas2)/2
    if nota>60:
            with open("camper.json", 'w') as outfile:
                json.dump(datos, outfile, indent=2)
                datos["estado"]="Aprobado"
    elif nota<60:
            with open("funciones1/camper.json", 'w') as outfile:
                json.dump(datos, outfile, indent=2)
                datos["estado"]="Desaprobado"


    with open("funciones1/camper.json","r") as file:
        datos = json.load(file)
    id_camper=str(input('Ingrese documento del camper'))
    for camp in camp:
        if camp["Documento"]==id_camper:
            nota1=int(input('ingrese nota de tareas: '))*0.10
            nota2=int(input('ingrese nota de filtros: '))*0.40
            nota3=int(input('ingrese nota de proyecto'))*0.60
            
            notaA = (nota1+nota2+nota3)
        
            if notaA>60:
                datos["estado"]="Cursando"
                with open("camper.json", 'w') as outfile:
                    json.dump(datos, outfile, indent=2)
            if notaA<60:
                datos["estado"]="filtrado"
                with open("camper.json", 'w') as outfile:
                    json.dump(datos, outfile, indent=2)
 
    

    

    






        
