# Librerias utilizadas
from fastapi import FastAPI
from fastapi.responses import HTMLResponse # Utilizado para generar el formato de texto de la pagina de inicio 
import pandas as pd
import calendar
import locale
import json 
import ast
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from collections import Counter
# Establecer el idioma en español
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

# Creacion de la App
app = FastAPI(title = "Project Data Engineer", description = "Henry's Data Engineering Project")

# Carga de csv con las transofrmaciones ya realizadas
df = pd.read_csv('Dataset/movies_final.csv', dtype={'popularity': str}, encoding='utf-8')

#Creamos una función index con mensaje de bienvenida
@app.get("/", response_class=HTMLResponse)
async def index ():
    output = "¡Bienvenido a la interfaz de consultas de catálogo de películas!. <br> <br>\
              Se cuenta con los siguiente 7 tipos de consultas (6 consultas generales y 1 consulta del sistema de recomendación).<br> <br>\
              Consulta 1: Cantidad de películas que se estrenaron en un mes dado históricamente. <br>\
              Consulta 2: Cantidad de películas que se estrenaron en un día dado históricamente. <br>\
              Consulta 3: Cantidad de películas, ganancia total y promedio dada una franquicia. <br>\
              Consulta 4: Cantidad de peliculas producidas en un país dado. <br>\
              Consulta 5: Ganancia total y la cantidad de peliculas que produjo una productora. <br>\
              Consulta 6: Inversion, la ganancia, el retorno y el año en el que se lanzó una película. <br>\
              Consulta 7: Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores. <br> <br>\
              Para conocer el formato de búsqueda, consulte el archivo README.md ubicado en el repositorio de GitHub. <br>"
    return output

# Se desarrollan las consultas que fueron solicitadas
# Consulta 1: Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes 
# (nombre del mes, en str, ejemplo 'enero') historicamente, return {'mes':mes, 'cantidad':respuesta}

@app.get("/peliculas_mes/")
def peliculas_mes(mes:str):
    # Convertir la columna "release_date" de object a datetime
    df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d', errors='coerce') # Se reemplaza las fechas dejando de lado los errores
    # Crear la columna release_month donde se extraerá el mes de la fecha de estreno.
    df['release_month'] = df['release_date'].apply(lambda x: x.month if x is not pd.NaT else None)
    df['release_month'] = df['release_month'].fillna(0).astype(int)
    meses = dict(enumerate(calendar.month_name))
    df['release_month'] = df['release_month'].map(meses)
    #meses = { i+1: calendar.month_name[i+1] for i in range(12) }
    #meses
    cantidad = df[df["release_month"] == mes]["release_month"].count()
    #print(cantidad)
    return f'Mes: {mes}, Cantidad: {cantidad}'
# Ejemplo de consulta testeada en deta: https://qlprmb.deta.dev/peliculas_mes/?mes=octubre

peliculas_mes('octubre')

# Consulta 2: Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente, return {'dia':dia, 'cantidad':respuesta}
@app.get("/peliculas_dia/")
def peliculas_dia(dia:str):
    # Convertir la columna "release_date" de object a datetime
    df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d', errors='coerce') # Se reemplaza las fechas dejando de lado los errores
    df["release_day"] = df['release_date'].dt.strftime('%A').apply(lambda x: x if type(x) != float else x)
    df["release_day"]
    respuesta = df[df["release_day"] == dia]["release_day"].count()
    return f'Día: {dia}, Cantidad: {respuesta}'

# Consulta 3: Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio, return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio':respuesta}
@app.get("/franquicia/")
def franquicia(franquicia:str):
    # Filtramos las filas que pertenecen a la franquicia deseada y contamos cuántas filas hay en el resultado filtrado.
    cantidad = df[df['name'] == franquicia].shape[0]
    
    df_franquicia = df[df['name'] == franquicia] # Filtra la franquicia solicitada

    # Calculamos la ganancia total
    gananciaTotal = (df_franquicia['revenue'] - df_franquicia['budget']).sum()
    gananciaPromedio = (df_franquicia['revenue'] - df_franquicia['budget'] / df_franquicia['budget']).mean()

    return f'Franquicia: {franquicia}, Cantidad: {cantidad}, Ganancia Total: {gananciaTotal}, Ganancia Promedio: {gananciaPromedio}'

# Consulta 4: Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo, return {'pais':pais, 'cantidad':respuesta}
@app.get("/peliculas_pais/")
def peliculas_pais(pais:str):
    mask = df['production_countries'].str.join(',').str.contains(pais, na=False)
   
    can = mask.count()
    # cantidad = df[mask]['title'].count()

    return f'pais: {pais}, cantidad:{can}'

# Consulta 5: Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron, return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}
@app.get("/productoras/")
def productoras(productora:str):
    prod = df[['name_production', 'budget', 'revenue']].dropna()
    prod ['name_production'] = prod['name_production'].map(str.lower)
    cantidad = prod.shape[0]
    gtotal= (prod['revenue'] - prod['budget']).sum()
    return {'productora':productora, 'ganancia_total': gtotal, 'cantidad': cantidad }

#productoras('Warner Bros.')'''
# Consulta 6: Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo, return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}
@app.get("/retorno/")
def retorno(pelicula:str):
    pelicula_data = df[df['title'] == pelicula]
    if len(pelicula_data) == 0:
        return f"No se encontró la película {pelicula}"
    inversion = pelicula_data['budget'].iloc[0]
    ganancia = pelicula_data['revenue'].iloc[0] - inversion
    retorno = ganancia / inversion if inversion > 0 else 0
    anio = int(pelicula_data['release_year'])
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio}

# ML

@app.get("/recomendacion/")
def recomendacion(titulo:str):
    df = pd.read_csv('Dataset/movies_ML.csv')
    
    tfidf = TfidfVectorizer(stop_words = 'english') #  Crea una instancia del objeto TfidfVectorizer que se utiliza para calcular la matriz
    df['overview'] = df['overview'].fillna('') # Rellena los valores faltantes (nulos) en la columna 'overview' del DataFrame 'df' con una cadena vacía ('')

    tfidf_matriz = tfidf.fit_transform(df['overview'])
    coseno_sim = linear_kernel(tfidf_matriz, tfidf_matriz) # Se utiliza para calcular la similitud de coseno
                                                           # La similitud de coseno es una medida comúnmente utilizada en procesamiento de texto para determinar la similitud entre dos documentos basándose en sus representaciones vectoriales
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    idx = indices[titulo] # Obtiene el índice correspondiente a un título de película específico en el objeto Series de índices creado anteriormente

    # Obtener el puntaje de similitud de esa pelicula con todas las películas
    simil = list(enumerate(coseno_sim[idx]))

    # Ordena las películas de acuerdo a su puntaje de similitud
    simil = sorted(simil, key=lambda x: x[1], reverse =True)

    # Obtiene el puntaje de similitud de 10 películas
    simil = simil[1:11]
    
    # Obtiene los índices 
    movie_index = [i[0] for i in simil]

    # Retorna 5 películas
    lista = df['title'].iloc[movie_index].to_list()[:5] 
      
    return {'lista recomendada': lista}