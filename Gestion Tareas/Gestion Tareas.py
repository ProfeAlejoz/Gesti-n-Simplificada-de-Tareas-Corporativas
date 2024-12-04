Hola hacer el G2

print("Bienvenido al bloc de notas")
for i in range(1000):
 nota=int(input("Presiona 1 para asignar una tarea y Presiona 2 para salir: ")) 
 if nota == 1:
    tarea=input("Escriba una tarea que sera asinada: ")
    print(f"La tarea {tarea} a sido asignada")
 elif nota == 2:
    print("Gracias por usar el bloc de notas")
    break
 else:
    print("Escriba un numero valido")       
 nota2=(input("¿Desea agregar una nueva tarea? (si/no): "))
 if nota2 == 'si':
    print("Asignemos otra tarea")
 elif nota2 == 'no':
    print("Gracias por usar el bloc de notas")
    break
 else:
    print("Escriba la opcion valida")             
