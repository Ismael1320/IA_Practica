user_word = input("Ingresa una palabara: ") #Solicita al usuario ingresar una palabra.

user_word = user_word.upper() #Convierte todas las letras de la palabras a mayúscula.

for letter in user_word: #Recorre cada letra de la palabra ingresada.

    if letter == "A": #Verifica si la letra actual es una vocal A.
        continue #Omite la letra y continúa con la siguiente interación del ciclo.
    
    elif letter == "E": #Verifica si la letra actual es una vocal E.
        continue #Omite la letra y continúa con la siguiente interación del ciclo.
    
    elif letter == "I": #Verifica si la letra actual es una vocal I.
        continue #Omite la letra y continúa con la siguiente interación del ciclo.
    
    elif letter == "O": #Verifica si la letra actual es una vocal O.
        continue #Omite la letra y continúa con la siguiente interación del ciclo.
    
    elif letter == "U": #Verifica si la letra actual es una vocal U.
        continue #Omite la letra y continúa con la siguiente interación del ciclo.
    
    else: #Si la letra no es vocal.
        print(letter) #Imprime la consonante.
