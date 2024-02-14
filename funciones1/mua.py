import json
def lista_campers():

    with open("camper.json") as file:
        inscritos = json.load(file)

    Options = input('¿Quieres agregar o actualizar? ')
    Options = Options.capitalize()

    if Options == 'Agregar':
        lista_campers = {
            "nombre": str(input("nombre: ")),
            "apellido1": str(input("apellido: ")),
            "apellido2": str(input("apellido2: ")),
            "direccion": str(input("direccion: ")),
            "acudiente": str(input("Acudiente: ")),
            "telefonos": str(input("Telefonos: ")),
            "Documento": str(input("Documento: ")),
            "Estado": str(input("Estado: ")),
            "Riesgo":  str(input("Riesgo: ")),
             }
    if lista_campers["Estado"].lower() == "inscrito":
        inscritos["campus"]["inscritos"].append(lista_campers)

        with open("camper.json", 'w') as outfile:
            json.dump(inscritos, outfile, indent=2)
    
    json.notas()

    if lista_campers["Estado"].lower() == "aprobado":
        inscritos["campus"]["aprobado"].append(lista_campers)
        
        with open("camper.json", 'w') as outfile:
            json.dump(inscritos, outfile, indent=2)

    if lista_campers["Estado"].lower() == "desaprobado":
        inscritos["campus"]["desaprobado"].append(lista_campers)
        
        with open("camper.json", 'w') as outfile:
            json.dump(inscritos, outfile, indent=2)

    if lista_campers["Estado"].lower() == "filtrado":
        inscritos["campus"]["filtrado"].append(lista_campers)
        
        with open("camper.json", 'w') as outfile:
            json.dump(inscritos, outfile, indent=2)

    if lista_campers["Estado"].lower() == "cursando":
        inscritos["campus"]["cursando"].append(lista_campers)
        
        with open("camper.json", 'w') as outfile:
            json.dump(inscritos, outfile, indent=2)

    if lista_campers["Estado"].lower() == "graduado":
        inscritos["campus"]["graduado"].append(lista_campers)
        
        with open("camper.json", 'w') as outfile:
            json.dump(inscritos, outfile, indent=2)

    if lista_campers["Estado"].lower() == "expulsado":
        inscritos["campus"]["expulsado"].append(lista_campers)
        
        with open("camper.json", 'w') as outfile:
            json.dump(inscritos, outfile, indent=2)

    if lista_campers["Estado"].lower() == "retirado":
        inscritos["campus"]["retirado"].append(lista_campers)
        
        with open("camper.json", 'w') as outfile:
            json.dump(inscritos, outfile, indent=2)