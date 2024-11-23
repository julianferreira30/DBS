# Tarea 3: Desarrollo de Aplicaciones Web
### Estudiante: Julián Ferreira

## Descripción
Para la tercera parte de la creación de la aplicación web fue necesaria la creación del apartado de comentario en las donaciones y un visualizador de datos. Este último son tablas con distinta información. Esto fue logrado con el uso de SQL y AJAX principalmente, además de Python y Javascript.

## Consideraciones
- Los comentarios tienen su respectiva validación de datos para evitar inyecciones maliciosas o indeseadas.
- El diseño de los gráficos se pensó en función de que eventualmente habrían muchos datos a mostrar, es por esto que las comunas son representadas en gráfico de barras y los dispositivos en un pie chart.
- Para los gráficos se ocupó la librería "Highcharts", lo que facilitó la implementación.

## Observaciones
- Para los gráficos se mostrarán todas las entradas de las donaciones, es decir, por ejemplo si un usuario de Valparaíso hace 3 donaciones simultáneamente, habrán 3 nuevas entradas en el gráfico de comunas asociada a la comuna de Valparaíso. Básicamente el gráfico es por dispositivos, no por usuario.