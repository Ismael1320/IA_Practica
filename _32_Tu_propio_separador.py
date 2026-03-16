def mysplit(strng): #Función que separa las palabras de una cadena.

    if strng == "": #Si la cadena esta vacía.
        return []   #Regresa una lista vacía.
        
    palabras = [] #Lista donde se guardarán las palabras.
    palabra = ""  #Variable para formar cada palabra.
    
    for caracter in strng: #Recorre cada carácter de la cadena.
        if caracter != " ": #Si no es un espacio.
            palabra += caracter #Agrega el carácter a la palabra.
            
        else: #Si encuentra un espacio.
            if palabra != "": #Siya se formó una palabra.
                palabras.append(palabra) #La guarda en la lista.
                palabra = "" #Reinicia la palabra.
                
    if palabra != "": #Si quedó una palabra al final.
        palabras.append(palabra) #La agrega a la lista.
        
    return palabras #Devuelve la lista de la palabras.

#Pruebas de la función    
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    