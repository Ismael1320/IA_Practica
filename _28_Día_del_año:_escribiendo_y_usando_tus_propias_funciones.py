def es_año_bisiesto(año):#Define una función que determina si un año es bisiesto.
   
    if año % 4 != 0: #Si el año no es divisible entre 4, es bisiesto.
       
        return False #Regresa un false indicando que el año es común.
    
    elif año % 100 != 0: #Si el año es divisible entre 4 pero no entre 100, es bisiesto.
        
        return True #Regresa un true indicando que el año es bisiesto.
   
    elif año % 400 != 0: #Si el año es divisible entre 100 pero no entre 400, es bisiesto.
       
        return False #Regresa un false indicando que el año es común.
    
    else: #Si el año es divisible entre 400.
        
        return True #Regresa un true indicando que el año es bisiesto.

def dias_en_el_mes(año,mes): #Define una función que devuelve la cantidadad de días de un mes en un año.
    
    if año < 1582 or mes < 1 or mes > 12: #Verifica si el año o mes están fuera del rango valido.
        
        return None #Devuelve non si los datos no son validos.
    
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #Lista con los días de cada mes en un año normal.
    
    res  = dias[mes - 1] #Obtiene los días del mes correspondiente (restando 1 por que los indices empiezan en 0).
    
    if mes == 2 and es_año_bisiesto(año): #Verifica si es febrero y el año es bisiesto.
        
        res = 29 #Si es febreo un año bisiesto, el mes tiene 29 dias.
    
    return res #Devuelve el número de días del mes.

def dia_del_año(año, mes, dia): #Función que calcula qué día del año es una fecha dada

    dias = 0 #Variable que acumula los días de los meses anteriores.
    
    for m in range(1, mes): #Recorre todos los meses anteriores al mes dado.
    
        md = dias_en_el_mes(año, m) #Obtiene los días del mes actual del ciclo.
    
        if md == None: #Verifica si el mes es valido.
    
            return None #Si es invalido devuelve un none.
    
        dias += md # Suma los días del mes al acumulador.
    
    md = dias_en_el_mes(año, mes) #Obtiene los días del mes actual.
    
    if dia >= 1 and dia <= md:  #Verifica que el día este dentro del rango válido del mes.
    
        return dias + dia #Devuelve el número total de días transcuridos en el año.
    
    else: #Verifica si el mes es valido.
    
        return None #Si es invalido devuelve un none.

print(dia_del_año(2000, 12, 31)) #Imprime el número de día del año para la fecha indicada.