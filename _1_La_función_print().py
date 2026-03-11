#Con esta linea se imprime un saludo en la pantalla
print("¡Hola, mundo!")

#Mientras que esta linea imprime el nombre del usuario
print("Jesus Ismael Flores Pardo")

#En estos casos manda anda un error de identidada inesperada
# print(Jesus Ismael Flores Pardo)
# print"Jesus Ismael Flores Pardo"
# print('Jesus Ismael Flores Pardo')
# print(Jesus Ismael Flores Pardo) print("¡Hola, mundo!")

#Si queremos forma que imprima el saludo con el nombre podemos hacer lo siguiente
print("\n",end="----------Otra forma----------\n")
print("¡Hola, mundo!","mi nombre es:", " Jesus Ismael Flores Pardo")

#O tambien lo podemos hacer declarando argumentos de palabra clave como lo es el end, 
#el cual nos permite colocaenviar una salida al final de nuestros argumentos posicionales.

print("\n",end="----------palabra clave end----------\n")
print("¡Hola, mundo!","mi nombre es: ", end="Jesus Ismael Flores Pardo\n")

#Existen diversas formas pero estos son algunos ejemplos