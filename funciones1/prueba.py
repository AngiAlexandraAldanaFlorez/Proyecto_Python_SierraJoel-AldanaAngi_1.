import json

ruta_json = 'Proyect/modulos/data/camper.json'
with open(ruta_json, 'r') as file:
    datos_json = json.load(file)

Options = input('¿Quieres agregar o actualizar ?')
Options = Options.capitalize()

if Options == 'Agregar':
        lista_campers = [{"nombre1"}]
        lista_campers[0] = str(input("Digite el primer nombre: "))
        datos_json[0](lista_campers)
        with open('Proyect/modulos/data/camper.json', 'w') as outfile:
               json.dump(datos_json, outfile , indent = str)

               pass

        lista_campers = {}
        lista_campers['nombre2'] = str(input("Digite el segundo nombre: "))
        datos_json['nombre2'].append(lista_campers)
        with open('Proyect/modulos/data/camper.json', 'w') as outfile:
               json.dump(datos_json, outfile , indent = 2)

               pass
        
        lista_campers = {}
        lista_campers['apellido1'] = str(input("Digite el primer apellido: "))
        datos_json['apellido1'].append(lista_campers)
        with open('Proyect/modulos/data/camper.json', 'w') as outfile:
               json.dump(datos_json, outfile , indent = 2)

               pass

        lista_campers = {}
        lista_campers['apellido2'] = str(input("Digite el segundo apellido: "))
        datos_json['apellido2'].append(lista_campers)
        with open('Proyect/modulos/data/camper.json', 'w') as outfile:
               json.dump(datos_json, outfile , indent = 2)
        
        pass
elif Options == 'Actualizar':


        pass
else:
        print('Opción no válida')
