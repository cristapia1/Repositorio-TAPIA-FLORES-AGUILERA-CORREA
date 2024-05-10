#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Se dirige al siguiente link: https://serviciomigraciones.cl/estudios-migratorios/estimaciones-de-extranjeros/
# Luego se presiona 2022 y se descarga  un archivo comprimido. Dentro del Archivo comprimido el que importa es el 'basecomunas.csv'

import pandas as pd
import unicodedata

#Se define la siguiente funcion para eliminar tildes y trabajar mas prolijo
def remove_accents(input_str):
    if pd.isna(input_str):
        return input_str  # Si es NaN, simplemente lo retorna sin cambios
    input_str = str(input_str)  # Asegurarse de que todos los datos son tratados como cadenas
    # Normalizar el texto para descomponer los tildes de las letras
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    # Remover los caracteres combinados (como tildes)
    only_ascii = nfkd_form.encode('ASCII', 'ignore').decode('utf-8')
    return only_ascii

# Se define la ruta al archivo
file_path = 'basecomunas.csv'

# Se carga el archivo en un DataFrame
df = pd.read_csv(file_path, encoding='ISO-8859-1')

    # Remover tildes
for column in ['SEXO', 'EDAD', 'PAIS', 'REGION', 'COMUNA']:
    df[column] = df[column].apply(remove_accents)


## Preparación de datos para análisis y visualización

# 1. Manejar valores nulos
df.fillna(0, inplace=True)

# 2. Los índices enteros son el año de estimación y la estimación de inmigrantes.
# Entonces, asegurarse de que el ano y el numero de inmigrantes sea un entero.
df['AÑO ESTIMACION'] = df['AÑO ESTIMACION'].astype(int)
df['ESTIMACION'] = df['ESTIMACION'].astype(int) 

# 3. Eliminar duplicados
df.drop_duplicates(inplace=True)

# 4. Filtrar datos irrelevantes
# Todas pueden ser relevantes para el estudio menos el desgloce de la 'ESTIMACION' de los inmigrantes
df = df[['SEXO', 'EDAD', 'PAIS', 'AÑO ESTIMACION', 'REGION', 'COMUNA', 'ESTIMACION']]

# 5. Se valida rango de años y de edad
df = df[(df['AÑO ESTIMACION'] >= 2018) & (df['AÑO ESTIMACION'] <= 2022)]
df = df[df['EDAD'].str.contains('A')] 
# Hasta el momento se trabaja con 'EDAD' como vino por 'default' es decir rangos de 5 en 5 anos y en formato como '00 A 04'
# No obstante si es que en un futuro se requiere cambiar la estructura de edad, se puede modificar su formato mas adelante

# 6. Se optimización los tipos de datos no numericos para categorías (menos uso de memoria, mejora el rendimiento, facilita su analisis)
df['SEXO'] = df['SEXO'].astype('category')
df['REGION'] = df['REGION'].astype('category')
df['COMUNA'] = df['COMUNA'].astype('category')
df['EDAD'] = df['EDAD'].astype('category')
df['PAIS'] = df['PAIS'].astype('category')

# 7. Verificar que no hay valores nulos
assert df.isnull().sum().sum() == 0

# Mostrar las primeras filas del DataFrame limpio
print(df.head())

# Opcional: Exportar a nuevo CSV
#df.to_csv('basecomunas_limpio.csv', index=False)

