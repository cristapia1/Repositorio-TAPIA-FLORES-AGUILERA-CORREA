# Cristopher Aguilera

## Explicacion limpieza de datos
- Descargué base de datos de delitos de connotación social en la provincia de Santiago entre 2018 y 2023 desde el portal CEAD. 
- Tuve que eliminar celdas innecesarias y cambiar tildes directamente desde Excel antes de importarlo al colab, además de cambiar la ubicación de la columnna "unidad territorial".
- Tuve problemas para visualizar el archivo, tuve que recurrir a la ayuda de un amigo y ChatGPT para poder ejecutar los comandos "latin_1" y el separador de ",".
- Para empezar la limpieza utilizé el código "dropna" para eliminar los valores nulos, posteriormente ejecuté "astype(str)" para tranformar las columnas de números en texto. Eso para despues con "replace" eliminar los ".", esto porque no podía eliminar los ceros sobrantes y la puntuación molestaba. Para terminar de dejar los números enteros con "replace" eliminé ",00", con eso los números estaban sin ceros ni comas. Finalmente utilizé "astype(int)" para que los números vuelvan a ser tratados como enteros en caso de ser nesesario para otro ejercicio.

## Fuentes y explicación

- Estadísticas delictuales: https://cead.spd.gov.cl/estadisticas-delictuales/. Elegimos estos datos para limpiar porque reflejan bien los cambios en el tiempo de las cifras delictuales en Santiago, y es una buena fuente para luego comparar y establecer relaciones con los otros datos sobre migración e inseguridad.

## Preguntas que se pueden responder

- ¿Qué tanto variaron las cifras nacionales de delitos de connotación social durante la pandemia?
- ¿Qué comunas han aumentado las cifras en comparación a la situación pre pandemia?
- ¿Qué comunas han bajado sus cifras en comparación a la situación pre pandemia?