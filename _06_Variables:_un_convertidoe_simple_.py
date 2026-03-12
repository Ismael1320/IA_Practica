kilometros = 12.25 #declaramos el valor para la variable kilometros
milllas = 7.38 #declaramos el valor para la variable millas

millas_a_kilometros = milllas*1.61 
#Ejecuta una operacio, la cual nos ayuda a convertir millas a kilometros y el resultado de esta sera el valor de nuestra variable

kilometros_a_millas = kilometros/1.61
#Ejecuta una operacio, la cual nos ayuda a convertir kilometros a millas y el resultado de esta sera el valor de nuestra variable


print(milllas, "millas son", round(millas_a_kilometros, 2), "kilómetros")#round redonde el valor de la variable
#Primero imprime le valor de millas, luego imprime el texto "millas son", despues imprime el valor de la converción redondeada a dos decimales 
#y finalmente impriem el texo "kilometro"

print(kilometros, "kilómetros son", round(kilometros_a_millas, 2), "millas")
#Primero imprime le valor de kilometro, luego imprime el texto "kilómetros son", despues imprime el valor de la converción redondeada a dos decimales 
#y finalmente impriem el texo "millas"