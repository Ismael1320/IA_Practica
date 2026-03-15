ingreso = float(input("Introduce el ingreso anual: "))#Le solicita al usuario el ingreso anual y loconvierte en decimal

if ingreso < 85528: # Verifica si el ingreso es menor al límite establecido.
	tax = ingreso * 0.18 - 556.02 #Calcula el impuesto aplicando el 18% del ingreso menos 556.02
    
else: # Si el ingreso es mayor o igual a 85528 se usa otra fórmula.
	tax = (ingreso - 85528) * 0.32 + 14839.02 #Calcula el impuesto aplicando el 32% al excedente y suam 14839.02

if tax < 0.0: # Verifica que el ingreso no sea negativo
	tax = 0.0 #Si el cálculo da negativo , el impuesto se ajusta a 0

tax = round(tax, 0) #Redonde el impuesto al numero más entero más cercano
print("El impuesto es:", tax, "pesos") #Muestra el impuesto total que debe pagar el usuario
 