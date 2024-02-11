
def options():
        opciones = input("ingrese un dato")
        if opciones == 1:
            ruta_json = 'Proyect/modulos/data/camper.json'
            with open(ruta_json, 'r') as camper_json:
                datos_json = json.load(camper_json)
            print(datos_json)

