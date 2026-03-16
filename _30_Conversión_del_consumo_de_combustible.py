def liters_100km_to_miles_gallon(litros): # Funcion que convierte litros por 100 km a millas por galon.
    millas = 100 / 1.609344  #convierte 100 km a millas.
    galones = litros / 3.785411784  #Convirte los litros consumidos a galones.
    return millas / galones #calcula cuantas millas se recorren por galón.

def miles_gallon_to_liters_100km(millas):  # Funcion que convierte  millas por galon a litros por 100 km.
    kilometro = millas * 1.609344 #Convierte las millas a kilometros.
    litros = 3.785411784 #Cantidad e litros en un galon.
    return litros/kilometro #Calcula cuántos litros se consumen en 100 km.

print(liters_100km_to_miles_gallon(3.9)) #Convierte 3.9 L/100km a mpg.
print(liters_100km_to_miles_gallon(7.5)) #Convierte 7.5 L/100km a mpg.
print(liters_100km_to_miles_gallon(10.)) #Convierte 10 L/100km a mpg.
print(miles_gallon_to_liters_100km(60.3)) #Convierte 60.3 L/100km a mpg.
print(miles_gallon_to_liters_100km(31.4)) #Convierte 31.4 L/100km a mpg.
print(miles_gallon_to_liters_100km(23.5)) #Convierte 23.5 L/100km a mpg.