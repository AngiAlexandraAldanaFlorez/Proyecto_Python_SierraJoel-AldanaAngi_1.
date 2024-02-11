import json

ruta_json = 'Proyect/modulos/data/camper.json'
with open(ruta_json, 'r') as file:
    datos_json = json.load(file)

Options = input('¿Quieres agregar o actualizar ?')
Options = Options.capitalize()

if Options == 'Agregar':
        lista_campers = {}
        lista_campers['Nombre'] = str(input("Digite su nombre: "))
        
        

        datos_json['Datos']['Inscritos'].append(lista_campers)
        with open('Proyect/modulos/data/camper.json', 'w') as outfile:
               json.dump(datos_json, outfile , indent = 2)
        
        pass
elif Options == 'Actualizar':


        pass
else:
        print('Opción no válida')
