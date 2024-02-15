import json
def notes():
    notas1=int(input('Ingrese la nota 1: '))
    notas2=int(input('Ingrese la nota 2: '))
    nota=(notas1+notas2)/2
    if nota>60:
            with open("camper.json", 'w') as outfile:
                json.dump(datos, outfile, indent=2)
                datos["Estado"]="Aprobado"
    elif nota<60:
            with open("funciones1/camper.json", 'w') as outfile:
                json.dump(datos, outfile, indent=2)
                datos["Estado"]="Desaprobado"


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

def options():
    
    with open("funciones1/camper.json","r") as file:
        inscritos = json.load(file)

        print('¿Quieres agregar o actualizar? ')
        Options = str(input('--> ')).lower()

        if Options == 'agregar':
            lista_campers = {
                "nombre": str(input("nombre: ")),
                "apellido1": str(input("apellido: ")),
                "apellido2": str(input("apellido2: ")),
                "direccion": str(input("direccion: ")),
                "acudiente": str(input("Acudiente: ")),
                "telefonos": str(input("Telefonos: ")),
                "Documento": str(input("Documento: ")),
                "Estado": "inscrito",
                "Riesgo":  " ",
                }

            
            with open("camper.json", 'w') as outfile:
                json.dump(inscritos, outfile, indent=4)
            
            print('¿Quieres ingresar las notas? (si/no)')
            ingre_notas=(str(input('--> ')))
            if ingre_notas=="Si" or ingre_notas=="si":
               notes()
            elif ingre_notas=="no" or ingre_notas=="No":
                    inscritos["campus"]["inscrito"].append(lista_campers)
                    with open("funciones1/camper.json", 'w') as outfile:
                            json.dump(inscritos, outfile, indent=2)
            
                    
        elif Options == 'actualizar':