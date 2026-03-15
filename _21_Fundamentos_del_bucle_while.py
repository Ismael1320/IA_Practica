blocks = int(input("Ingresa el número de bloques: ")) #Se pide al usuario la cantidad de bloques.

height = 0 #Variable que guarda la altura de la piramide.
capa = 1 #Cantidad de bloques necesarios para la capa actual.

while blocks >= capa: #El ciclo continúa mientras haya blouqes suficientes.
    blocks = blocks - capa  # Se restan los bloques utilizados en la capa.
    height += 1  # Se incrementa la altura porque se completó una capa.
    capa += 1  # La siguiente capa necesitará un bloque más.
    
else: #Este bloque se ejecuta cuando el while termina porque ya no hay bloques suficientes.
    print("Las capas de la pirámide:",capa) #Muestra el número real de capas contruidas
    print("\n\nLa altura de la pirámide:", height) #Muestra la altura de la piramide