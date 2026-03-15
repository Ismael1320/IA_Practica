secret_number = 777 #Se define el numero secreto que el usuario debe de adivinar

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""") #Muesta un mensaje de bienvenida y las intruccioness de juego

numero=int(input()) #Solicita al ususario un número entero para intentar adivinar el número secreto

while numero != secret_number: #Ciclo se ejecuta mientras el número ingresado sea diferente al número secreto
    
    if numero != secret_number: #Verifica nuevamente que el número no sea el correcto
        print(
"""
+===========================================+
| ¡Ja, ja! ¡Estás atrapado en mi bucle!     |
| Si quieres salir de aqui debes de adivinar|
| Anda vulve a intentar                     |
+===========================================+
""") #Muestra un mensaje indicando que el usuario debe volver a intentar

    numero=int(input()) #Vuelve a pedir otro número al ususario para intentar adivinar nuevamente.

print("\n\n¡",numero,"!") #Muestra el número correcto cuando el usuario lo adivina
print(
"""
+===========================================+
| ¡Bien hecho, muggle! Eres libre ahora!    |
+===========================================+
""") #Muestra un mensaje final felicitando al usuario por adivinar el número