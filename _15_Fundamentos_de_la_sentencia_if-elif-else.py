año = int(input("Introduce un año: "))#Le solicita al usuario que ingrese un año

if año < 1582: #Verifica si el año es menor a 1582
	print(año, "no esta dentro del período del calendario Gregoriano")#Si año es menor a 1582 muestra el siguiente mensaje
	

else: #Si año es año es mayor a 1582 se ejecutaran los siguientes posibles casos
	
	if año % 4 != 0: #Si el año no es divisible entre 4, es decir su residuo es diferente de 0 entoces se imprime el mensaje de abajo.
		print("El año",año,"es un año Común") #Si el residuo de la división entre 4 es diferente a 0, entonces es un año comun
		
	elif año % 100 != 0: #Si el año no es divisible entre 100, es decir su residuo es diferente de 0 entoces se imprime el mensaje de abajo.
		print("El año",año,", es un año Bisiesto")#Si el residuo de la división entre 100 es diferente a 0, entonces es un año bisisesto
	
	elif año % 400 != 0: #Si el año no es divisible entre 400, es decir su residuo es diferente de 0 entoces se imprime el mensaje de abajo.
		print("El año",año,"es un año Común") #Si el residuo de la división entre 400 es diferente a 0, entonces es un año comun
		
	else: #Si el año es divisible entre culquiera de los casos anteriores entoces se imprime el mensaje de abajo.
		print("El año",año,"es un año Bisiesto") #Si el año si es divisible entre culquiera de los casos, entonces es un año bisisesto