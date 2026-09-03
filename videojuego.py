print("Bienvenido a CUAC EL DEMOLEDOR")

input("Presiona ENTER para continuar")
print("\nJUGAR")
print("NIVEL 1")

turno_jugador = True

if turno_jugador:
    print("\nEs tu turno")

    print("\n MENÚ ")
    print("1. Colocar bloque")
    print("2. Reparar bloque")
    print("3. Comprar poder")
    opcion = input("Elige una opción: ")

    if opcion == "Colocar bloque":
        print("Has colocado un bloque.")
    elif opcion == "Reparar bloque":
        print("Has reparado un bloque.")
    elif opcion == "Compar poder":
        print("Has comprado un poder.")
    else:
        print("Opción no válida.")
        
else:
    print("Esperando turno...")
    print("Volviendo a JUGAR...")



