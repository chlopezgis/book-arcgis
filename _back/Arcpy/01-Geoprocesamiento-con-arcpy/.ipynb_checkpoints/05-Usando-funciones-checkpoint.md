# **Usando funciones**

* Las funciones en Python **realizan tareas específicas**.

* Casi todas las **herramientas de geoprocesamiento** en ArcGIS Pro **son funciones** en ArcPy.

* ArcPy ofrece varias **funciones que no son herramientas**.

* Estas otras funciones pueden **listar**, **verificar**, **recuperar** y **validar datos**, y están diseñadas para flujos de trabajo en Python.

* Las funciones tienen parámetros y devuelven valores, con una sintaxis similar a las herramientas:

```python
arcpy.<nombredefunción>(<argumentos>)
```

Por ejemplo, el siguiente código determina si un conjunto de datos existe y luego imprime Verdadero o Falso:

```python
import arcpy
print(arcpy.Exists("C:/Data/streams.shp"))
```

La función **`arcpy.Exists()`** devuelve un valor booleano. Otras funciones devuelven otros tipos de valores, incluidos cadenas y números.
