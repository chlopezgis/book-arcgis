# **Trabajando con objetos Result**

## **¿Qué es un objeto Result?**

Un objeto _Result_ es lo que se obtiene como **resultado de ejecutar una herramienta en ArcPy**. Es como una caja que **contiene la salida de la herramienta**.
  
>El objeto _Result_ **se puede utilizar como entrada para otra función**.

## **¿Qué contiene un objeto Result?**

Un objeto _Result_ en ArcPy puede contener varios tipos de información, incluyendo:

* **`Ruta de la salida a un nuevo archivo`**: Si la herramienta produce una nueva capa de entidad o actualiza una existente, el objeto Result **puede incluir la ruta al conjunto de datos resultante**.

* **`Datos adicionales`**: La salida del objeto Result puede ser una **cadena de texto**, un **número** o un valor **booleano**, dependiendo del tipo de herramienta y su resultado.

* **`Mensajes de ejecución`**: Puede contener **mensajes generados durante la ejecución de la herramienta**, que pueden ser útiles para diagnosticar problemas o entender el proceso de ejecución.

* **`Parámetros utilizados`**: Los **parámetros de entrada de la herramienta, junto con sus valores**, pueden estar incluidos en el objeto Result, lo que proporciona un registro de los parámetros utilizados en la ejecución de la herramienta.

## Ejemplos

1. Se ejecuta la herramienta de geoprocesamiento `GetCount_management` y la salida se devuelve un número entero como un objeto Result:

```python
import arcpy
arcpy.env.workspace = "C:/Data"
mycount = arcpy.GetCount_management("streams.shp")
print(mycount)
```
Este código muestra la representación del objeto Result, por ejemplo: 3153

2. El siguiente código ejecuta la herramienta de geoprocesamiento Clip y la salida devuelve la ruta de salida a la nueva entidad creada:

```python
import arcpy
arcpy.env.workspace = "C:/Data"
myresult = arcpy.Clip_analysis("streams.shp", "study.shp", "result.shp")
print(myresult)
```

Ejecutar el código muestra la representación en cadena de la ruta al conjunto de datos de salida: `C:/Data/result.shp`

3. En el siguiente código, se crea un bufer para una clase de entidad utilizando la herramienta Buffer. La clase de entidad poligonal de salida se devuelve como un objeto y se utiliza como entrada para la herramienta Get Count, de la siguiente manera:

```python
import arcpy
arcpy.env.workspace = "C:/Data/study.gdb"
buffer = arcpy.Buffer_analysis("str", "str_buf", "100 METERS")
count = arcpy.GetCount_management(buffer)
print(count)
```
