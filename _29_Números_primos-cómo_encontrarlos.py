def is_prime(num): #Define una funciónque verifica si es un número primo.

    for i in range(2, int(1 + num ** 0.5)): #Recorre los posibles divisores desde dos hasta la raiz cuadrada de un número.

        if num % i == 0: #Verifica si el número es divisible exactamente por i.

            return False #Si tiene un divisor, no es primo y devuelve un false.
        
    return True #Si no se encontraron divisores, el número es primo y devuelve true

for i in range(1, 20): #Crea un ciclo que recorre números del 1 al 19.

    if is_prime(i + 1): #LLama a la función para verificar si l número es primo.

        print(i + 1, end=" ") #Imprime el número primo en la misma línea separado por espacios.

print(" son números primos.") #Imprime un mensaje final indicando que los números mostrados son primos.