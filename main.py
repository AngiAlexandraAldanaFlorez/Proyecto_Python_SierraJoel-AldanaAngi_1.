import json

print("╔══════ Bienvenido ══════╗")
print("║                        ║")
print("╚════════════════════════╝")

print('¿Quién eres?')

roles = int(input('''\t1. Coordinadora
      \t2. Trainer
      \t3. Salir
        '''))

if roles == 1:
    print('Administración')
    print('¿Qué quieres ver?')

    opciones = int(input('''\t1. Campers
      \t2. Trainers
      \t3. Rutas
      \t4. Salas
      \t5. Test
      '''))

    if opciones == 1:
        with open("funciones1/camper.json", "r") as file:
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
                "Riesgo": " ",
            }

            with open("camper.json", 'w') as outfile:
                json.dump(inscritos, outfile, indent=4)

            print('¿Quieres ingresar las notas? (si/no)')
            ingre_notas = (str(input('--> ')))
            if ingre_notas == "Si" or ingre_notas == "si":
                with open("funciones1/camper.json", "r") as file:
                    inscritos = json.load(file)
                notas1 = int(input('Ingrese la nota 1: '))
                notas2 = int(input('Ingrese la nota 2: '))
                nota = (notas1 + notas2) / 2
                if 60 > nota:
                    inscritos['Estado'] = "Desaprobado"
                    inscritos["nota"] = ("", nota)
                    print("Este camper fue desaprobado con una nota de:", nota)
                elif 60 < nota:
                    inscritos['Estado'] = "Aprobado"
                    inscritos["nota"] = ("", nota)
                    print("Este camper fue aprobado con una nota de:", nota)

                    # Aquí se agrega el camper a la sala correspondiente
                    with open("salones.json", "r") as sala_file:
                        salones_data = json.load(sala_file)

                    seccion = None
                    for key in salones_data.keys():
                        if len(salones_data[key]) < 33:
                            seccion = key
                            break

                    if seccion:
                        salones_data[seccion].append(inscritos)
                        print("Camper agregado a la sección", seccion)
                    else:
                        print("No hay secciones disponibles para agregar aprobados.")
                else:
                    inscritos['Estado'] = "Desaprobado"
                    inscritos["nota"] = ("", nota)
                    print("Este camper fue desaprobado con una nota de:", nota)

                    # Resto del código para notas y manejo de archivos

                with open("funciones1/camper.json", "w") as file:
                    json.dump(inscritos, file, indent=4)

                with open("salones.json", "w") as sala_file:
                    json.dump(salones_data, sala_file, indent=4)
        elif Options == 'actualizar':
            with open("funciones1/camper.json","r") as file:
                  datos = json.load(file)
                  camp=datos["campus"]
                  id_camper=str(input('Ingrese documento del camper'))
                  for camp in camp:
                        if camp["Documento"]==id_camper:
                              nota1=int(input('ingrese nota de tareas: '))*0.10
                              nota2=int(input('ingrese nota de filtros: '))*0.40
                              nota3=int(input('ingrese nota de proyecto'))*0.60
                  
                              final = (nota1+nota2+nota3)
            
                              if final >=  65:
                                    camp['Estado'] = "cursando"  
                                    camp["nota"] = ("nota final es:",final) 
                                    print("¡Este camper ha aprobado el filtro mensual con una nota final de", final)
                              else:
                                   final < 65
                                   camp['Estado'] = "filtrado"   
                                   camp["nota"] = "la nota es",final
                                   print("El camper esta en riego, Su nota final es", final)
                                                
                        else:
                              print("Camper no encontrado.")  
                              break   
                         
                    
                      
                        with open("JSON/Campers.json", "w") as outfile:
                              json.dump(datos, outfile, indent=4)
   

       
           
