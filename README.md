# AyEDJAAR2023

Repositorio de AyED - Maestria en Ciencias de la Computacion UNSA

#Integrantes

- Jesus Alpaca Rendon jalpacare@unsa.edu.pe

## Proyectos
# EJERCICIO #1

* Desarrollar una comparasion entre Goland, Python y C++. Dicha comparasion debe realizarse
en terminos de tiempo de procesamiento. Usted debera implementar cuatro (04) programas en
los tres (03) lenguages y luego medir el tiempo de procesamiento.
* Los programas a implementar pueden ser: Algoritmo de burbuja para ordenar listas, Algoritmo
Quick sort, Algoritmo Merge sort, Solucion al problema de n-reinas, etc. Recuerde que debe
implementar 04 programas, pueden ser tomados de internet pero debe ser el mismo algoritmo en
los tres lenguajes.
* Para medir el tiempo de procesamiento considere:
    • Debe realizar el experimento en una misma computadora.
    • Debe ejecutar el coodigo minimo 5 veces y luego obtener el promedio de tiempo de procesamiento
    y la desviacion estandar.
    • Debe medir el tiempo para diferentes tama~nos de entrada, por ejemplo si implementa algun
    algoritmo de ordenamiento, debera realizar los experimentos para listas de tama~no: 100,
    1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000 y 50000.
    • Una vez obtenga el tiempo de procesamiento para diferentes tama~nos de entrada y para los
    tres lenguajes debera generar una imagen similar a la Figura 1. Puede usar Matlplotlib.

* Debera desarrollar un informe con el siguiente contenido:
    • Introduccion.
    • Algoritmos (los 04 algoritmos que va a implementar, tambien debe incluir el costo computacional).
    • Implementacion (enlace a Github).
    • Resultados.
        - Tabla comparativa con el promedio de tiempo de procesamiento y desviacion estandar.
        - Graficos.
    • Conclusiones.
# EJECUCION DEL PROYECTO

## REQUERIMIENTOS
 * Golang(https://go.dev/doc/install)
 * Python(https://www.python.org/downloads/)
 * C++:
    - MSYS2(https://github.com/msys2/msys2-installer/releases/download/2023-05-26/msys2-x86_64-20230526.exe)
    - Extension C/C++ Visual Studio Code(https://code.visualstudio.com/docs/cpp/config-mingw)
## PASOS
 * Golang:
    En la ruta de los archivos goland ejecutar el siguiente comando para construir el ejecutable:
    ```go build <archivo.go>```
    Ahora en Windows, ejecutar el .exe con el argumento de la ruta de la lista de numeros a ordenar con el algoritmo:
    ```./mergeSort.exe ../Data/50000_data.txt```
    Se generara 2 archivos de texto, uno con el resultado de la lista ordenada y otro en la carpeta Resultados/Golang con el tiempo de demora de la ejecucion

 * Python:
    En la ruta de los archivos python ejecutar el siguiente comando para ejecutar el .py,de igual manera con la ruta de la lista de numeros como argumento:
    ```python <archivo.py> ../Data/50000_data.txt```    
    Se generara 2 archivos de texto, uno con el resultado de la lista ordenada y otro en la carpeta Resultados/Python con el tiempo de demora de la ejecucion

 * C++:
    En la ruta de los archivos C++ ejecutar el siguiente comando para construir el ejecutable:
    ```g++ <archivo.cpp>```
    Ahora en Windows, ejecutar el .exe(se genera con el nombre a.exe por defecto) con el argumento de la ruta de la lista de numeros a ordenar con el algoritmo:
    ```./a.exe ../Data/50000_data.txt```
    Se generara 2 archivos de texto, uno con el resultado de la lista ordenada y otro en la carpeta Resultados/C++ con el tiempo de demora de la ejecucion

 * Estadisticas
    Una vez obtenidos todos los datos, nos ubicamos en la carpeta Results y ejecutamos el script stadistics.py de la siguiente manera por ejemplo:
    ```python stadistics.py '.\\C++' C++ selectionSort```
    Los parametros a cambiar seran la ruta de los archivos con los tiempos que estan separados por lenguaje, el lenguaje a calcular y el algoritmo seleccionado.
    Obtendremos un .csv como resultado con la desviacion estandar, el limite maximo y limite minimo.
  * Graficas
    Para las graficas, nos ubicamos en la misma carpeta y ejecutamos el siguiente comando por ejemplo:
    ```python graphics.py quick 40000```
    Genera el grafico comparativo por tama;o de datos y algoritmo en la carpeta Graficos
# RESOLUCION

* Algoritmos seleccionados:
    - Binary Insertion Sort
    - Bubble sort
    - Quick sort
    - Selection sort
    - Merge sort

# TAREAS
## 2023-07-29 TODO
    * Jesus: Informe en Latex
    * Luis Borit: Matplotlib
    * Abel: Juntar los algoritmos en un solo proyecto
    * TODOS: Desarrollar cada uno por su lado los algoritmos con la finalidad de entenderlos y seleccionar los finales el dia martes

## 2023-08-03 UPDATE

Por temas personales, no pude completar mi parte y para no perjdicar a mis compañeros en la presentacion de su trabajo, decidi realizarlo por mi cuenta.
Se llego a consenso con ellos de que se entregaria el dia jueves pero lamentablemente no llegue a la fecha, por lo que ellos presentaran aparte su informe.
Actualmente a la fecha, se sube los resultados de los tiempos de ejecucion en los 3 lenguajes para los diferentes tamaños de datos, ejecutados en una misma computadora

## 2023-08-04 PREVIEW

Se subio el informe en su version PDF, el archivo latex ya se tenia previamente en el repositorio por el tema del versionamiento, por lo que fue actualizado al igual que las tablas comparativas que se añadieron en el informe final.

## 2023-08-04 FINAL

Informe completo


