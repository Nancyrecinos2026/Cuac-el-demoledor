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

print("\nTURNO DEL ENEMIGO")
print("1. Nimcy el Mapache")
print("2. Cris el Topo")
print("3. Cuac el Pato")
enemigo = input("Elige un enemigo: ")
if enemigo == "1":
    print("Nimcy roba un bloque.")
elif enemigo == "2":
    print("Cris emerge de la tierra.")
elif enemigo == "3":
    print("Cuac destruye dos bloques.")
else:
    print("Enemigo no válido.")

print("\nVERIFICAR DERROTA")

princesa = input("¿La princesa recibió daño? (si/no): ")

if princesa == "si":
    print("¡La princesa recibió daño!")
else:
    print("La princesa está a salvo.")

base = input("¿La base fue destruida? (si/no): ")

if base == "si":
    print("GAME OVER")
    print("La base fue destruida.")
else:
    print("La base sigue en pie.")

if princesa == "no" and base == "no":

    print("\nVERIFICAR VICTORIA")

    enemigo_derrotado = input("¿Derrotaste al enemigo? (si/no): ")

    if enemigo_derrotado == "si":
        print("¡GANASTE EL NIVEL 1!")
        print("Recibes monedas.")
    else:
        print("No derrotaste al enemigo.")
        print("Pierdes.")

