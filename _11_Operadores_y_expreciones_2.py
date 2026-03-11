H = int(input("Hora de inicio (horas): ")) #Se pide al usuario ingresar la hora de inicio del evento y H almacenara las horas ingresadas
Min = int(input("Minuto de inicio (minutos): ")) #Se pide al usuario ingresar minuto de inicio del evento y Min almacenara los minutos ingresadas
Dur = int(input("Duración del evento (minutos): ")) #Se pide al usuario ingresar la duración del evento y Dur almacenara la duración

Min = Min + Dur #Se suman los minutos iniciales con la duración del evento
H = H + Min // 60 #Min//60 calculas las horas completas que hay en los minutos y se los suma a las horas
Min = Min % 60 #Obtiene los minutos restantes despues de convertir a horas
H = H % 24 #Asegura que la hora se mantenga en un rango de 24 horas

print("\nTerminara a las= ",H,":",Min)#Se imprimira la hora en la que terminará el evento