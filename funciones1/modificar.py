import json

with open("camper.json","r") as file:
    inscritos = json.load(file)

print('¿Quieres agregar o actualizar? ')
Options = str(input('--> '))
Options = Options.capitalize()

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
        notas1=int(input('Ingrese la nota 1: '))
        notas2=int(input('Ingrese la nota 2: '))
        nota=(notas1+notas2)/2
        if nota>60:
            inscritos["campus"]["aprobado"].append(lista_campers)
            with open("funciones1/camper.json", 'w') as outfile:
                json.dump(inscritos, outfile, indent=2)
        elif nota<60:
            inscritos["campus"]["desaprobado"].append(lista_campers)
            with open("funciones1/camper.json", 'w') as outfile:
                json.dump(inscritos, outfile, indent=2)
    elif ingre_notas=="no" or ingre_notas=="No":
            inscritos["campus"]["inscrito"].append(lista_campers)
            with open("funciones1/camper.json", 'w') as outfile:
                    json.dump(inscritos, outfile, indent=2)
                
elif Options == 'actualizar':
    documento = input('Ingresa el documento del camper que deseas actualizar')
    
    for camper in inscritos["campus"]:
        if documento == camper.get('Documento'):
            print(f'El documento a actualizar es {documento}')
            break
    else:
        print('no se puede')  
