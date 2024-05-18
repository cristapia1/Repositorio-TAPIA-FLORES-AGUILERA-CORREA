##  Cristian Tapia

Eliminé casillas y cambié tildes desde Excel para evitar problemas al importar al colab.
Ejecute astype(str) para poder eliminar “.0”
Con replace reemplacé “.0” y “nan” por nada para que desaparezcan
Por último, con df.to_csv guardé los datos limpios en drive en formato csv

# Explicación

fuente: https://cead.spd.gov.cl/estadisticas-delictuales/

- estos datos nos permiten ver como ha variado el rango de edad principalmente de los victimarios de delitos de connotacion social entre 2018 y 2023, los seleccionamos porque podemos establecer comparaciones con las cifras de inmigracion

## Preguntas

¿Que sexo ha sufrido mayor cantidad de delitos en el periodo establecido?
¿Que sexo altero mas sus cifras delictuales como victimarios durante el periodo?
¿Cual es el rango de edad de victimarios que mas vario en los años de pandemia?