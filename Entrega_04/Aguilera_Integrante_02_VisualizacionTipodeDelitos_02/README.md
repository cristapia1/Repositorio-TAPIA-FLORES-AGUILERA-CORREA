
## Selección de datos y visualización

Los datos fueron elegidos pensando en el enfoque de graficar que delitos habían aumentado más o menos en cantidad en la provincia de Santiago en el periodo de 2018-2023. Con ese objetivo, decidí elegir los dos de los delitos que más aumentaron, en este caso fueron: homicidios y robo con sorpresa. Y dos de los que más disminuyeron fueron: robo en lugar habitado e infracción a la ley de armas.

En primer momento tomé la decisión de graficar en Flourish todos los delitos con sus cifras por separado para que sea más fácil de entender, teniendo en cuenta lo dispar de los números entre delitos. El primer intento eran gráficos horizontales, pero creí que era complicar la comprensión.

Despues me enteré que el resultado final tenia que ser en Google Colab y con códigos de Python y Markdown para realizar la visualización.
Para poder hacerlo primero importe las librerías y monte mi drive. Después tuve que revisar videos en Youtube y ChatGPT para poder graficar con la librería “matplotlib”. Cuando más o menos entendí lo que hice fue elegir los valores que quería graficar. Una vez elegidos borré los delitos que no iba a representar. Por último, para hacer el gráfico utilicé “ax=valores.plot.bar” y descargué el resultado. Hice el mismo proceso para cada año que quise representar. Lo que no pude conseguir fue hacer que las letras sean más pequeñas o que la imagen del gráfico sea más grande, esto porque las letras se superponen y empeoran el entendimiento.


La visualización responde a preguntas como:

¿Qué delitos fueron los que más aumentaron desde el 2018 hasta la fecha?
¿En qué cantidad y porcentaje aumentaron esos delitos?
¿Qué delitos fueron los que disminuyeron más sus cifras desde el 2018?
¿En qué cantidad y porcentaje disminuyeron esos delitos?

