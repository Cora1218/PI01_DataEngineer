# PI01_DataEngineer
# ![image](https://github.com/Cora1218/PI_01_DataEngineer/assets/105570983/d5435320-5aa0-4088-9567-7db7aaffc9e9)

# PROYECTO INDIVIDUAL N°1 - DATA ENGINEER (Henry´s bootcamp)
# Desarrollado por María Guadalupe Martínez Jiménez 
* Problemática: 
El área de análisis de datos solicita al de Data engineering que realice consultas para un sistema de recomendación de películas, utilizando un dataset provisto, 
para ésto debe realizar las transformaciones requeridas y posteriormente ponga a disposición los datos mediante la elaboración y ejecución de una API.

* Rol del desarrollador:
Data Engineer.
# Proceso de "ETL" (Extract, transform, load) en VisualStudioCode - Python:
# EXTRACCIÓN DE DATOS
* Importación de la librería pandas para el manejo de dataframes.
* Ingesta de datos (movies_dataset.csv provistos por el cliente).
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

ML
* def recomendacion(titulo): '''Toma como parámetro el título de una película y retorna una lista de 5 películas recomendadas de acuerdo al título'''

Nota: El desarrolo de las consultas se encuentra alojado en el archivo funcionesApi.ipynb.

# Proceso para el desarrollo de la API, utilizando FastAPI (framework que permite construir APIs con Python) y Render para realizar el deploy:
* Generación de archivo main.py (donde desarrollar el script) y otro requirements.txt (donde alojar los requerimientos para la API).
* Importación de las librerías a utilizar.
* Declaración de la creación de la API.
* Declaración de la ruta de acceso para la base de datos a utilizar.
* Creación de un directorio índex con mensaje de bienvenida a la interfaz.
* Desarrollo de las consultas con formato:
  
  @app.get("/tipo_de_consulta/")
  def tipo_de_consulta(variable1:tipo_de_dato, variable"n":...):
  desarrollo_de_la_funcion.
  
# Creación de un entorno virtual
* python -m venv venv: Para instalar dependencias y librerías.
* Una vez creado el micro, se realizan las pruebas correspondientes a las consultas con el endpoint URL provisto por deta.
# Crear archivos necesarios (desde Gitbash)
* touch .gitignore
* touch main.py
* touch requirements.txt
# venv + .gitignore
* Poner '/venv' dentro del archivo .gitignore

# FastApi y Render
Desde la terminal de VSCode, realizar los siguientes pasos:
* git init
* pip install uvicorn
* pip install fastapi

# Pip freeze
* pip freeze > requirements.txt (Solo las necesarias).
  - Si luego se necesita instalar otra librería más, se vuelve a ejecutar este comando.

Ahora ya puedes codear toda tu API con Fastapi (main.py).

# Creación repo Github
* Crear un nuevo repo en Github (Dejarlo en modo público).
 - Comunicarnos desde el repositorio local con Github.
* git config user.name y git config user.email vamos a introducir
  nuestros datos para poder conectarnos con el repositorio remoto.
* Para comunicar los archivos locales con la repo remota usamos git remote
  add origin y entre comillas, la url de nuestro repo.
* Desde una terminal en VSC poner: git add . (añadimos todos los
  archivos que tienen cambios.)
* git commit -m y el nombre del commit entre comillas.
* Con git push -u origin master vamos a hacer la conexión con Github.
  Master o main son la rama principal con la que vamos a trabajar. Origin es
  el nombre por convención que le ponemos a nuestro repositorio.
¡Ahora otros usuarios van a poder ver nuestro repo!

# Render
1.- Entrar en render.com y crearse una nueva cuenta de usuario.

2.- Elegir la opción Web Service.

3.- Ir al apartado que se encuentra abajo de Public Git repository. Copiar y pegar el enlace del repositorio que crearon anteriormente (recuerden que sea público).

4.- Llenar los campos necesarios. En branch seleccionen main. Runtime tiene que ser Python 3.

5.- El resto de los campos se deben llenar con la misma información que en la imagen: 

![image](https://github.com/Cora1218/PI01_DataEngineer/assets/105570983/66d8082e-c091-4dcd-b128-c4b4dbd68076)
6.- Seleccionar la opción Create Web Service.

7.- Una vez terminados los pasos anteriores, se va a comenzar a cargar nuestra aplicación. Puede tardar unos minutos.

8.- Entrar al enlace de arriba a la izquierda.

9.- Nos va a direccionar a nuestra API. Si les aparece un "Not found", agregar un /docs a su enlace.

¡Con todos esos pasos, la API que crearon ya está lista para poder ser consumida!

# Instrucciones para la utilización de la Api:
Ingrese al siguiente URL: https://renderapihenry.onrender.com

De acuerdo a la consulta que quiera solicitar, debera agregarle a continuación del URL la consulta y variables con el siguiente formato:

* Consulta 1: .../peliculas_mes/?mes=octubre (En el entorno virtual si funciona porque tengo importado la libreía locale para establecer el idioma Español     locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8') y en render ya no lo acepró a pesar de ponerle la dependencia en requirements.tx).

  Ejemplo de búsqueda: https://renderapihenry.onrender.com/peliculas_mes/?mes=octubre Se esperaría --> 'Mes: octubre, Cantidad: 4614'
  
* Consulta 2: .../peliculas_dia/?dia=martes (En el entorno virtual si funciona porque tengo importado la libreía locale para establecer el idioma Español     locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8') y en render ya no lo acepró a pesar de ponerle la dependencia en requirements.tx).

  Ejemplo de búsqueda: https://renderapihenry.onrender.com/peliculas_dia/?dia=martes Se esperaría --> 'Día: martes, Cantidad: 4640'
  
* Consulta 3: .../franquicia/?franquicia=Toy%20Story%20Collection

  Ejemplo de búsqueda: https://renderapihenry.onrender.com/franquicia/?franquicia=Toy%20Story%20Collection Se esperaría --> 'Franquicia: Toy Story Collection, Cantidad: 3, Ganancia Total: 343554033.0, Ganancia Promedio: 373554032.0'
  
* Consulta 4: .../peliculas_pais/?pais=United%20States%20of%20America

  Ejemplo de búsqueda: https://renderapihenry.onrender.com/peliculas_pais/?pais=United%20States%20of%20America Se esperaría --> 'pais: United States of America, cantidad:45372'
  
* Consulta 5: .../productoras/?productora=Warner Bros.

  Ejemplo de búsqueda: https://renderapihenry.onrender.com/productoras/?productora=Warner%20Bros. Se esperaría --> {'productora': 'Warner Bros.', 'ganancia_total': 317932254772.0, 'cantidad': 33573}

* Consulta 6: .../retorno/?pelicula=Toy%20Story

  Ejemplo de búsqueda: https://renderapihenry.onrender.com/retorno/?pelicula=Toy%20Story Se esperaría --> {"pelicula":"Toy Story","inversion":30000000.0,"ganancia":343554033.0,"retorno":11.4518011,"anio":1995}

* consulta 7: .../recomendacion/?titulo=Toy%20Story del sistema de recomendación (En entorno virtual si funciona en Render no :( ).

  Ejemplo de búsqueda: https://renderapihenry.onrender.com/recomendacion/?titulo=Toy%20Story Se esperaría --> {'lista recomendada': ['Toy Story 2', 'The Champ', 'Rebel Without a Cause', 'Man on the Moon','Malice']}
Las variables pueden ser reemplazadas en el formato de consulta por el elemento deseado:

* mes: Puede ser cualquier mes del año (enero, febrero...diciembre). (En entorno virtual si funciona por el import de locale para el idioma español en        Render no me lo permitió).
* dia: Puede ser reemplazado por cualquier día de la semana (lunes, martes...domingo). (En entorno virtual si funciona por el import de locale para el     idioma español en Render no me lo permitió).
* franquicia: Cualquier nombre de franquicia o colección a la que pertenece la película (Toy Story Collection, Grumpy Old Men Collection, Father of the Bride Collection, etc.). 
* pais: País donde se produjo la película (United States of America, United Kingdom, etc.).
* pelicula: Título de alguna película (Toy Story, Jumanji, Balto, etc).

Nota: Para conocer mas detalles técnicos acerca de las funciones y sus respectivos parámetros puede ingresar a https://renderapihenry.onrender.com/docs
Link de la API en producción.

# Tecnologías y herramientas utilizadas: 
* Visual studio code 

* Python 

* Pandas

* FastApi 

* Render

* Uvicorn 
  
