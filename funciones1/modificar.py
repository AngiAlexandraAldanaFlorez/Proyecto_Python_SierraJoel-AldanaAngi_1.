import json

ruta_json = 'Proyect/modulos/data/camper.json'
with open(ruta_json, 'r') as file:
    datos_json = json.load(file)

Options = input('¿Quieres agregar o actualizar? ')
Options = Options.capitalize()

if Options == 'Agregar':
    
    nombre = str(input("Digite su nombre: "))
    apellido1 = str(input("Digite su primer apellido: "))
    
    datos_json['nombre'] = nombre
    datos_json['apellido1'] = apellido1

    
    with open('Proyect/modulos/data/camper.json', 'w') as outfile:
        json.dump(datos_json, outfile, indent=2)
elif Options == 'Actualizar':


        pass
else:
        print('Opción no válida')
