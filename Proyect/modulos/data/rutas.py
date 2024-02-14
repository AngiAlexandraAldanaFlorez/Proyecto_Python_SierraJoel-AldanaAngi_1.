import json

def crearJsonRutas():
    datos = {
        "NodeJS": [],
        "Java": [],
        "NetCore": [],
    }
    jsonData = json.dumps(datos, indent=4)

    rutaArchivo = "rutas.json"
    with open(rutaArchivo, 'w') as archivo:
        archivo.write(jsonData)

    return rutaArchivo

jsonGeneracion = crearJsonRutas()

def imprimirJsonRuta():
    rutaJson = "rutas.json"

    with open(rutaJson, 'r') as f:
        json_data = json.load(f)
        for ruta, sub_rutas in json_data.items():
            print(f"{ruta}: {sub_rutas}")

def agregarSubRuta(ruta_archivo, ruta, nuevo_item):
    with open(ruta_archivo, 'r') as t:
        jsonDato = json.load(t)
        if ruta in jsonDato:
            jsonDato[ruta].append(nuevo_item)
        else:
            print(f"La ruta {ruta} no existe en el JSON.")
            return

    with open(ruta_archivo, 'w') as file:
        json.dump(jsonDato, file, indent=4)

def optionRutas():
    print("Menu de opciones:\n1 Agregar subRutas\n2 Eliminar subrutas\n3 Actualizar subrutas\n4 Ver Sub Rutas actuales")
    answerR = int(input())
    if answerR == 1:
        print("¿En qué ruta deseas agregar? (NodeJS, Java, NetCore)")
        imprimirJsonRuta()
        answer_r = input()
        if answer_r.lower() in ["nodejs", "java", "netcore"]:
            print("¿Cuántas sub rutas vas a ingresar?")
            num_rutas = int(input())
            if num_rutas > 0:
                ruta_json = 'rutas.json'
                for i in range(num_rutas):
                    nuevoItemUsuario = input(f"Ingrese la sub Ruta {i+1} para {answer_r}\n")
                    agregarSubRuta(ruta_json, answer_r, nuevoItemUsuario)
                with open(ruta_json, 'r') as j:
                    jsonDato = json.load(j)
                    print(json.dumps(jsonDato, indent=4))

print("Actualmente manejamos 3 rutas principales:")
imprimirJsonRuta()
optionRutas()


