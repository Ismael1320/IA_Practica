def is_year_leap(year): #Define una función que determina si un año es bisiesto.
    if year % 4 != 0: #Si el año no es divisible entre 4, es bisiesto.
        return False #Regresa un false indicando que el año es común.
    elif year % 100 != 0: #Si el año es divisible entre 4 pero no entre 100, es bisiesto.
        return True #Regresa un true indicando que el año es bisiesto.
    elif year % 400 != 0: #Si el año es divisible entre 100 pero no entre 400, es bisiesto.
        return False #Regresa un false indicando que el año es común.
    else: #Si el año es divisible entre 400.
        return True #Regresa un true indicando que el año es bisiesto.

test_data = [1900, 2000, 2016, 1987] #Lista de años que se usaran para probar la función. 
test_results = [False, True, True, False] #Resultados esperados para cada año de prueba.
for i in range(len(test_data)): #Recorre la lista de datos de prueba usandosus índices.
    yr = test_data[i] #Guarda el año actual que se esta evaluando.
    print(yr,"-> ",end="") #Imprime el año evaluadosin cambiar de línea.
    result = is_year_leap(yr) #llama a la función para verificar si el año es bisiesto.
    if result == test_results[i]: #Compara el resultado obtenido con el esperado.
        print("OK") #Si coincide la prueba es correcta.
    else: #Si el resultdo no coincide.
        print("Fallido") #Indica que la prueba falló.
