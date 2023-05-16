# PI01_DataEngineer
# ![image](https://github.com/Cora1218/PI_01_DataEngineer/assets/105570983/d5435320-5aa0-4088-9567-7db7aaffc9e9)

# PROYECTO INDIVIDUAL N°1 - DATA ENGINEER (Henry´s bootcamp)
# Desarrollado por María Guadalupe Martínez Jiménez 
* Problemática: 
El área de análisis de datos solicita al de Data engineering que relaice un sistema de recomendación de películas, utilizando un grupo de datasets provistos, 
para ésto debe realizar las transformaciones requeridas y posteriormente ponga a disposición los datos mediante la elaboración y ejecución de una API.

* Rol del desarrollador:
Data engineer.
# Proceso de "ETL" (Extract, transform, load) en VisualStudioCode - Python:
# EXTRACCIÓN DE DATOS
* Importación de la librería pandas para el manejo de dataframes.
* Ingesta de datos (Archivo .csv provistos por el cliente).
* Análisis exploratorio para conocer sus características principales.

# TRANSFORMACIONES

* Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila,
  ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.
* Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.
* Los valores nulos del campo release date deben eliminarse.
* De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.
* Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.
* Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.
* Exportar CSV final con todas las transformaciones.

Nota: La extracción de datos así como las respectivas transformaciones pueden verse desarrolladas en el archivo transformacionPlataformas.ipynb.

# Desarrollo de las consultas solicitadas:

* def peliculas_mes(mes): '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente''' return {'mes':mes, 'cantidad':respuesta}

* def peliculas_dia(dia): '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente''' return {'dia':dia, 'cantidad':respuesta}

* def franquicia(franquicia): '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio''' return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio':respuesta}

* def peliculas_pais(pais): '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo''' return {'pais':pais, 'cantidad':respuesta}

* def productoras(productora): '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron''' return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}

* def retorno(pelicula): '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo''' return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}

Nota: El desarrolo de las consultas se encuentra alojado en el archivo funcionesApi.ipynb.

# Proceso para el desarrollo de la API, utilizando FastAPI (framework que permite construir APIs con Python) y Deta para realizar el deploy:
* Generación de archivo main.py (donde desarrollar el script) y otro requirements.txt (donde alojar los requerimientos para la API).
* Importación de las librerías a utilizar.
* Declaración de la creación de la API.
* Declaración de la ruta de acceso para la base de datos a utilizar.
* Creación de un directorio índex con mensaje de bienvenida a la interfaz
* Desarrollo de las consultas con formato:
  
  @app.get("/tipo_de_consulta/")
  def tipo_de_consulta(variable1:tipo_de_dato, variable"n":...):
  desarrollo_de_la_funcion.
* Creacion de una cuenta en Deta.
* Instalacion del Deta CLI en consola de forma local mediante comando "iwr https://get.deta.dev/cli.ps1 -useb | iex"
* Comprobación de la correcta instalacion con "deta --help"
* Login en deta a través de la consola mediante comando "deta login"
* Ubicado en el path de la carpeta donde se encuentra la API desarrollada se procede a la creacion de un micro mediante el comando "deta new"
* Una vez creado el micro, se realizan las pruebas correspondientes a las consultas con el endpoint URL provisto por deta.

# Instrucciones para la utilización de la herramienta:
Ingrese al siguiente URL: https://fastapideta1-1-y1445592.deta.app

De acuerdo a la consulta que quiera solicitar, debera agregarle a continuación del URL la consulta y variables con el siguiente formato:

* Consulta 1: .../peliculas_mes/?mes=octubre
* Consulta 2: .../peliculas_dia/?dia=martes
* Consulta 3: .../franquicia/?franquicia=Toy%20Story%20Collection
* Consulta 4: .../peliculas_pais/?pais=United%20States%20of%20America
* Consulta 5: .../
* Consulta 6: .../retorno/?pelicula=Toy%20Story

Las variables pueden ser reemplazadas en el formato de consulta por el elemento deseado:

* mes: Puede ser cualquier mes del año (enero, febrero...diciembre).
* dia: Puede ser reemplazado por cualquier día de la semana (lunes, martes...domingo).
* franquicia: Cualquier nombre de franquicia o colección a la que pertenece la película (Toy Story Collection, Grumpy Old Men Collection, Father of the Bride Collection, etc.). 
* pais: País donde se produjo la película (United States of America, United Kingdom, etc.).
* pelicula: Título de alguna película (Toy Story, Jumanji, Balto, etc).

# Ejemplos de búsquedas:
* Consulta 1: https://fastapideta1-1-y1445592.deta.app/peliculas_mes/?mes=octubre
* Consulta 2: https://fastapideta1-1-y1445592.deta.app/peliculas_dia/?dia=martes
* Consulta 3: https://fastapideta1-1-y1445592.deta.app/franquicia/?franquicia=Toy%20Story%20Collection
* Consulta 4: https://fastapideta1-1-y1445592.deta.app/peliculas_pais/?pais=United%20States%20of%20America
* Consulta 5:
* Consulta 6: https://fastapideta1-1-y1445592.deta.app/retorno/?pelicula=Toy%20Story

Nota: Para conocer mas detalles técnicos acerca de las funciones y sus respectivos parámetros puede ingresar a https://fastapideta1-1-y1445592.deta.app/docs
Link de la API en producción.

# Tecnologías utilizadas: 
* Visual studio code 

* Python 

* Deta cloud 

* FastApi 

* Uvicorn 

* Pandas library 
