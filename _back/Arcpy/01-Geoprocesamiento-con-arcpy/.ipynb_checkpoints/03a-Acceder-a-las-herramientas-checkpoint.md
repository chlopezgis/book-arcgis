# **Acceder a las herramientas de geoprocesamiento**

`ArcPy` proporciona acceso a todas las herramientas de geoprocesamiento en ArcGIS Pro (dependiendo del tipo de licencia). Estas herramientas se pueden llamar desde ArcPy utilizando: El **`nombre`** y el **`alias de la caja de herramientas`** a la que pertenecen.

![image](https://github.com/chlopezgis/cl-programacion-gis/assets/88239150/c99fee24-39a7-421e-a311-aa283f2947d1)

Hay dos formas de acceder a las herramientas de geoprocesamiento desde ArcPy:

### **1. Utilizando una función**

La forma más fácil de usar una herramienta es llamar a su función correspondiente.

**Sintaxis**

```python
arcpy.<nombreherramienta_aliascajaherramientas>(<parámetros>)
```

**Ejemplo**

```python
arcpy.Clip_analysis("streams.shp", "study.shp", "result.shp")
```

### **2. Utilizando la estructura de modulos de arcpy**

Una forma alternativa de acceder a una herramienta es primero llamar a la caja de herramientas como un módulo y luego la herramienta como una función de este módulo, seguido de los parámetros de la herramienta.

**Sintaxis**

```python
arcpy.<aliascajaherramientas>.<nombreherramienta>(<parámetros>)
```

**Ejemplo**

```python
arcpy.analysis.Clip("streams.shp", "study.shp", "result.shp")
```

### _**NOTA**_

_En ArcPy, el alias de la caja de herramientas se utiliza para acceder a las herramientas de geoprocesamiento de manera más eficiente y **evitar conflictos entre herramientas con nombres similares** pero **ubicadas en diferentes cajas de herramientas**. Por ejemplo, existen múltiples herramientas de "Clip": una en la caja de herramientas de Análisis (es decir, "Clip") y otra en la caja de herramientas de Administración de Datos (es decir, "Clip Raster", pero el nombre en ArcPy es "Clip")_
