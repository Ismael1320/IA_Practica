my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9] #Se crea una lista con números, algunos repetidos.

numeros_sin_repetir = [] #Se crea una lista vacía donde se gurdaran los numeros sin repetirse.

for num in my_list: #Recorre cada número de la lista original.
    
    if num not in numeros_sin_repetir: #Verifica que el número aún no está en la lista.
        numeros_sin_repetir.append(num) #Si no está repetido, se agrega a la lista de numeros_sin_repetir
        
my_list = numeros_sin_repetir #Se reemplaza la lista original por la lista sin elementos repetidos.

print("La lista con elementos únicos:") #Muestra un mensaje indicando que se imprimirá la lista sin duplicados.
print(my_list) #Imprime la lista final con solo números únicos.