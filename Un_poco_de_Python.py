print("""
+-------------------------------------------------------------------------+
|Bienvenido a Python.                                                     |
|Python es un lenguaje de programación de alto nivel, interpretado,       |
|orientado a objetos y de uso generalizado con semántica dinámica, que se |
|utiliza para la programación de propósito general.                       |
|                                                                         |
|¿Te gustaria saber algo sobre Python?                                    |
|                                                                         |
|1. ¿De donde proviene la palabra Python                                  | 
|2. ¿Quien lo creo?                                                       |
|3. ¿Cuales son sus objetivos?                                            |
|4. ¿Existe más de un Python?                                             |
|5. ¿Dónde podemos ver a Python en acción?                                |
|6.Menu                                                                   |
|7.Salir                                                                  |
+-------------------------------------------------------------------------+
""")

while True:
    
    opcion = input("""
Introdusca el numero de la opcion que quiere ver.
Si no recureda las opciones introdusca 6 para regresar al menu: 
""")


    if opcion == "1":
        print("""
+--------------------------------------------------------------------------+
|Aunque puede que conozcas a la pitón como una gran serpiente, el nombre   |
|del lenguaje de programación Python proviene de una vieja serie de        |
|comedia de la BBC llamada Monty Python's Flying Circus.                   |
|                                                                          |
|En el apogeo de su éxito, el equipo de Monty Python estaba realizando sus | 
|escenas en vivo para audiencias en todo el mundo, incluso en el Hollywood |
|Bowl.                                                                     |
|                                                                          |
|Dado que Monty Python es considerado uno de los dos nutrientes            |
|fundamentales para un programador (el otro es la pizza), el creador de    |
|Python nombró el lenguaje en honor al programa de televisión.             |
+--------------------------------------------------------------------------+
          """)
        continue
        
    
    if opcion == "2":
        print("""
+-------------------------------------------------------------------------+
|Python fue creado por Guido van Rossum, nacido en 1956 en Haarlem,       |
|Países Bajos.                                                            |
|Por supuesto, Guido van Rossum no desarrolló y evolucionó todos los      |
|componentes  de Python. La velocidad con la que Python se ha extendido   |
|por todo el mundo es el resultado del trabajo continuo de miles de       |
|(muy a menudo anónimos) programadores, testers, usuarios (muchos de ellos| 
|no son especialistas en TI) y entusiastas, pero hay que decir que la     | 
|primera idea (la semilla de la que brotó Python) llegó a una cabeza: la  |
|de Guido.                                                                |
+-------------------------------------------------------------------------+
          """)
        continue
    
    if opcion == "3":
        print("""
+-------------------------------------------------------------------------+
|En 1999, Guido van Rossum definió sus objetivos para Python:             |
|                                                                         |
|*Un lenguaje fácil e intuitivo tan poderoso como los de los principales  |
| competidores.                                                           |
|                                                                         |
|*De código abierto, para que cualquiera pueda contribuir a su desarrollo.|
|                                                                         |
|*El código que es tan comprensible como el inglés simple.                |
|                                                                         |
|*Adecuado para tareas cotidianas, permitiendo tiempos de desarrollo      |
| cortos.                                                                 |
+-------------------------------------------------------------------------+
          """)
        continue
    
    
    if opcion == "4":
        print("""
+---------------------------------------------------------------------------------+
|Existen dos tipos principales de Python, llamados Python 2 y Python 3.           |
|                                                                                 |          
|Python 2 es una versión anterior del Python original. Su desarrollo se ha        |
|estancado intencionalmente, aunque eso no significa que no haya actualizaciones. |
|Por el contrario, las actualizaciones se emiten de forma regular, pero no        |
|pretenden modificar el idioma de manera significativa. Prefieren arreglar        |
|cualquier error recién descubierto y agujeros de seguridad. La ruta de desarrollo|
|de Python 2 ya ha llegado a un callejón sin salida, pero Python 2 en sí todavía  |
|está muy vivo.                                                                   |
|                                                                                 |
|Python 3 es la versión más nueva (para ser precisos, la actual) del lenguaje.    |
|Está atravesando su propio camino de evolución, creando sus propios estándares y |
|hábitos.                                                                         |
+---------------------------------------------------------------------------------+
          """)
        continue

    if opcion == "5":
        print("""
+---------------------------------------------------------------------------------+
|Lo vemos todos los días y en casi todas partes. Se utiliza ampliamente para      | 
|implementar complejos Servicios de Internet como motores de búsqueda,            |
|almacenamiento en la nube y herramientas, redes sociales, etc. Cuando utilizas   | 
|cualquiera de estos servicios, en realidad estás muy cerca de Python.            |
|                                                                                 |
|Muchas herramientas de desarrollo se implementan en Python. Cada vez se escriben |
|más aplicaciones de uso diario en Python. Muchos científicos han abandonado las  |
|costosas herramientas patentadas y se han cambiado a Python. Muchos testers de   |
|proyectos de TI han comenzado a usar Python para llevar a cabo procedimientos de | 
|prueba repetibles. La lista es larga.                                            |
+---------------------------------------------------------------------------------+
          """)
        continue  

    if opcion == "6":
        print("""
+-------------------------------------------------------------------------+
|Bienvenido a Python.                                                     |
|Python es un lenguaje de programación de alto nivel, interpretado,       |
|orientado a objetos y de uso generalizado con semántica dinámica, que se |
|utiliza para la programación de propósito general.                       |
|                                                                         |
|¿Te gustaria saber algo sobre Python?                                    |
|                                                                         |
|1. ¿De donde proviene la palabra Python                                  | 
|2. ¿Quien lo creo?                                                       |
|3. ¿Cuales son sus objetivos?                                            |
|4. ¿Existe más de un Python?                                             |
|5. ¿Dónde podemos ver a Python en acción?                                |
|6.Menu                                                                   |
|7.Salir                                                                  |
+-------------------------------------------------------------------------+
""")
        continue      
  
    if opcion == "7":
        print("""
+-------------------------------------------------------------------------+
|                  Ahora conoces un poco mas de Python.                   |
|                                                                         |
|                            ¡Nos vemos pronto!                           |
+-------------------------------------------------------------------------+
          """)
        break
    

    else:
        print("Esa opcion no es valida.", end = " ")
        continue

