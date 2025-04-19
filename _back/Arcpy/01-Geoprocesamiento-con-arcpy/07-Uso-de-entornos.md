# **Uso de entornos**

Los entornos se exponen como propiedades de la clase **`env`**. Estas propiedades recuperan los valores actuales o los establecen. La sintaxis para acceder a las propiedades de la clase **`env`** es:


```python
arcpy.env.<propiedad>
```

La clase **`env`** tiene muchas otras propiedades. Se puede encontrar una lista completa en la documentación de ArcPy. Algunas propiedades importantes incluyen el espacio de trabajo, la extensión, el sistema de coordenadas de salida, el espacio de trabajo temporal y el dominio XY. Algunas propiedades son específicas para las clases de entidades o para los conjuntos de datos raster.

## 1. **Establecer valores**

### **Establecer el espacio de trabajo `Workspace`**

Para establecer el espacio de trabajo actual, utiliza el siguiente código:

```python
import arcpy
arcpy.env.workspace = "C:/Data"
```

### **Establecer el tamaño de celda `cellsize`**

El siguiente código establece el tamaño de celda en 30:

```python
import arcpy
arcpy.env.cellSize = 30
```
Este código significa que cualquier raster de salida creado por herramientas de geoprocesamiento se creará con un tamaño de celda de 30, independientemente del tamaño de celda de los raster de entrada. La unidad está establecida por el sistema de coordenadas para las salidas, otro entorno.

### **Configurar la sobreescritura de la salida `overwriteOutput`**

Las opciones de geoprocesamiento incluyen la opción de permitir que las herramientas de geoprocesamiento sobrescriban conjuntos de datos existentes. En ArcPy, sobrescribir es una propiedad de la clase **`env`**. El valor predeterminado de esta propiedad **`overwriteOutput`** es **_"False"_**. El siguiente código **establece el valor en _"True"_**:

```python
import arcpy
arcpy.env.overwriteOutput = True
```

Al probar el código, es común establecer esta propiedad en tu script porque permite sobrescribir la salida de ejecuciones anteriores del mismo script sin tener que eliminar manualmente los archivos o renombrar las salidas.

## 2. **Recuperar valores**

Las propiedades de la clase **`env`** no solo especifican entornos para ejecutar herramientas de geoprocesamiento, sino que también se pueden usar para recuperar sus valores actuales

### **Recuperar la toleranciaXY**

El siguiente código recupera la configuración actual para la tolerancia XY:

```python
import arcpy
print(arcpy.env.XYTolerance)
```

Ejecutar el código imprime el valor actual del parámetro de Tolerancia XY. El valor predeterminado de None se imprime a menos que el valor se haya establecido previamente.

## 3. **Listar todas las propiedades de la clase `env`**

Para ver una lista completa de todas las propiedades de la clase env, usa la función `dir()` de la siguiente manera:

```python
import arcpy
print(dir(arcpy.env))
```

El resultado es:

```
['MDomain', 'MResolution', 'MTolerance', ...]
```
