# Patrones de los dígitos (5 filas por número)
digitos = [
["###",
 "# #",
 "# #",
 "# #",
 "###"],  # 0

["  #",
 "  #",
 "  #",
 "  #",
 "  #"],  # 1

["###",
 "  #",
 "###",
 "#  ",
 "###"],  # 2

["###",
 "  #",
 "###",
 "  #",
 "###"],  # 3

["# #",
 "# #",
 "###",
 "  #",
 "  #"],  # 4

["###",
 "#  ",
 "###",
 "  #",
 "###"],  # 5

["###",
 "#  ",
 "###",
 "# #",
 "###"],  # 6

["###",
 "  #",
 "  #",
 "  #",
 "  #"],  # 7

["###",
 "# #",
 "###",
 "# #",
 "###"],  # 8

["###",
 "# #",
 "###",
 "  #",
 "###"]   # 9
]

# Pedir número al usuario
numero = input("Introduce un número: ")

# Imprimir el display
for fila in range(5):  # Cada número tiene 5 filas
    for digito in numero:
        print(digitos[int(digito)][fila], end=" ")
    print()