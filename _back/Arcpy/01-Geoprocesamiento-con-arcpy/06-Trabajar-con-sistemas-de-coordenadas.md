# **Trabajar con sistemas de coordenadas**

## 1. **Obtener el CRS utilizando `Describe`**

Para determinar la información de referencia espacial de cualquier conjunto de datos, incluyendo clases de entidades, conjuntos de datos ráster, TINs, etc., puedes utilizar las funciones **`arcpy.Describe()`** o **`arcpy.da.Describe()`**.

```python
# Import module
import arcpy
import os

# 1. Workspace
path = r'D:\Charlie\02_Cursos\02_PROGRAMACION_GIS\ARCPY\Aprendizaje\00-datos'

# 2. Input FC
data = 'Precip2008Readings.shp'

# 3. Describe CRS of the input
desc = arcpy.Describe(os.path.join(path, data))
print(desc.spatialReference.name)
```

## 2. **Obtener el CRS por el nombre**

Otra alternativa para obtener el CRS es usar el nombre del sistema de coordenadas:

```python
sr = arcpy.SpatialReference("NAD 1983 StatePlane Texas Central FIPS 4203 (US Feet)")
print(sr.name)
```
El nombre de la proyección utilizado como parámetro de entrada para la clase **`SpatialReference`** y la propiedad **`name`** no son idénticos, lo que puede causar confusión. Por ejemplo, el resultado del código anterior es el siguiente:

```
NAD_1983_StatePlane_Texas_Central_FIPS_4203_Feet
```

Los espacios en el nombre de la proyección se reemplazan por guiones bajos (_) en la propiedad **"name"**. Otra diferencia es la omisión de unidades en la propiedad **"name"**.

## 3. **Obtener el CRS por el código EPSG (WKID)**

Otra alternativa es usar el código de fábrica, también conocido como ID bien conocido (WKID). El siguiente ejemplo utiliza el WKID y luego imprime el nombre, tipo y unidades lineales del sistema de coordenadas:

```python
sr = arcpy.SpatialReference(32718)
print(sr.name)
print(sr.type)
print(sr.linearUnitName)
```

El resultado es:

```
WGS_1984_UTM_Zone_18S
Projected
Meter
```
