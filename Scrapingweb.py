import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime

fecha_y_hora_actual = datetime.datetime.now()

fecha_y_hora_actual_formateada = fecha_y_hora_actual.strftime('%d/%m/%Y %H:%M:%S')

# URL del sitio web
url = 'https://www.dieselogasolina.com/incidencias-carreteras-trafico-A-5.html'

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}

# Realizamos la solicitud a la página
page = requests.get(url, headers=headers)

# Creamos el objeto BeautifulSoup y analizamos el contenido HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Encontramos la tabla con el id="lista_incidencias"
table = soup.find('table', {'id': 'lista_incidencias'})

#Comprobamos si la tabla esta en la web
if table is not None:

    # Obtenemos todas las filas de la tabla
    rows = table.find_all('tr')

    # Creamos las listas para cada columna de la tabla
    fechas = []
    niveles = []
    tipos = []
    poblaciones = []
    crtas = []
    kilometros = []
    sentidos = []

    # Iteramos sobre cada fila de la tabla y obtenemos los datos de cada celda
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 7:
            fechas.append(cells[0].text.strip())
            niveles.append(cells[1].find('img')['src'])
            tipos.append(cells[2].text.strip())
            poblaciones.append(cells[3].text.strip())
            crtas.append(cells[4].text.strip())
            kilometros.append(cells[5].text.strip())
            sentidos.append(cells[6].text.strip())

    # Creamos un diccionario con las listas de cada columna
    data = {
        'Fecha': fechas,
        'Nivel': niveles,
        'Tipo': tipos,
        'Poblacion': poblaciones,
        'Crta': crtas,
        'Kilometro': kilometros,
        'Sentido': sentidos
    }

    # Creamos un DataFrame de pandas con el diccionario
    df = pd.DataFrame(data)

    # Remplaza en la columna nivel el texto por un icono
    df['Nivel'] = df['Nivel'].replace('https://cdn.dieselogasolina.com/images/icons/green_trafico.png', '🟢 Tráfico fluido')
    df['Nivel'] = df['Nivel'].replace('https://cdn.dieselogasolina.com/images/icons/NO APLICA_trafico.png', '⚪ Sin Datos')
    df['Nivel'] = df['Nivel'].replace('https://cdn.dieselogasolina.com/images/icons/yellow_trafico.png', '🟡 Tráfico irregular')
    df['Nivel'] = df['Nivel'].replace('https://cdn.dieselogasolina.com/images/icons/red_trafico.png', '🔴 Tráfico difícil')
    df['Nivel'] = df['Nivel'].replace('https://cdn.dieselogasolina.com/images/icons/black_trafico.png', '⚫ Tráfico interrumpido')

    # Remplaza en la columna nivel el texto por un icono
    df['Tipo'] = df['Tipo'].replace('OBRAS', '🚧 OBRAS')

    # Remplaza s por una s y un espacio para separar la hora del texto
    df["Fecha"] = df["Fecha"].str.replace("s", "s ")

    # filtrar las líneas que contienen 'hoy' en la columna Fecha
    df_filtrado = df[df['Fecha'].str.contains('Hoy')];

    # Insertar dos nuevas columnas para los valores de kilometraje superior e inferior
    df_filtrado.insert(1, 'Km_Superior', 0)
    df_filtrado.insert(2, 'Km_Inferior', 0)


    # Separar la cadena de texto en dos valores numéricos
    df_filtrado = df.copy()  # Asegúrate de trabajar con una copia del DataFrame original
    df_filtrado[['Km_Superior', 'Km_Inferior']] = df_filtrado['Kilometro'].str.split(' al ', expand=True).astype(float)


    
    # Filtrar las columnas con Km_superior o Km inferior al KM60
    df_filtrado = df_filtrado[(df_filtrado['Km_Superior'] < 60) | (df_filtrado['Km_Inferior'] < 60)]


    # imprimir el DataFrame filtrado
    #print(df_filtrado)
    
    code_html = '⬇️🚗 <b>ESTADO DEL TRAFICO A-5</b> 🚗⬇️ ' + (fecha_y_hora_actual_formateada)
    if df_filtrado.empty == False:
        for i in range(len(df_filtrado)):
            code_html=code_html + '\n\n <b>Fecha:</b> ' + str((df_filtrado['Fecha'].iloc[i])) +'\n <b>Nivel:</b> ' + str((df_filtrado['Nivel'].iloc[i])) +'\n <b>Tipo:</b> ' + str((df_filtrado['Tipo'].iloc[i])) +'\n <b>Poblacion:</b> ' + str((df_filtrado['Poblacion'].iloc[i])) +'\n <b>Crta:</b> ' + str((df_filtrado['Crta'].iloc[i])) +'\n <b>Kilometro:</b> ' + str((df_filtrado['Kilometro'].iloc[i])) +'\n <b>Sentido:</b> ' + str((df_filtrado['Sentido'].iloc[i]))  

else:
    code_html="✅ SIN INCIDENCIAS DE TRAFICO ✅"
