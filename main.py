import funciones1.modificar as modi

print("╔══════ Bienvenido ══════╗")
print("║                        ║")
print("╚════════════════════════╝")

print('¿Quien eres?')

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
      modi.options()

       
           
