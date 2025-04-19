# **Trabajando con mensajes**

Para hacer que la ejecución de scripts independientes sea más informativa, puedes obtener mensajes de geoprocesamiento desde el propio script utilizando la función **`arcpy.GetMessages()`**

Todos los mensajes tienen una **`propiedad de severidad`**. Esta propiedad es un entero con un valor de: 0 (Información), 1 (Advertencia) y 2 (Error). La Tabla 1 describe estos tres niveles de severidad con más detalle.


|Nivel de severidad|Descripción|
|------------------|-----------|
|**severity = 0 (mensaje informativo)**|Este tipo de mensaje proporciona información sobre la ejecución. Esto incluye información general como el progreso de la herramienta, la hora de inicio y finalización de la herramienta, e información sobre los resultados de la herramienta. Nunca se usan para indicar problemas.|
|**severity = 1 (mensaje de advertencia)**|Los mensajes de advertencia indican un posible problema. Esto podría ser una situación que puede causar un problema durante la ejecución de la herramienta o una situación en la que el resultado puede no ser el esperado. Los mensajes de advertencia no impedirán que una herramienta se ejecute, pero sí ameritan una inspección.|
|**severity = 2 (mensaje de error)**|Los mensajes de error indican que una situación impide la ejecución de la herramienta. Por lo general, esto significa que una o más configuraciones de parámetros son inválidas.|

Los mensajes de advertencia y error incluyen un código de identificación de seis dígitos documentado, útil para identificar las causas de problemas y sus soluciones potenciales.

ArcPy mantiene los mensajes del último proceso ejecutado, accesibles mediante **`GetMessages()`**. Esta función devuelve una cadena con todos los mensajes de la herramienta ejecutada recientemente, permitiendo filtrarlos según su severidad.

La sintaxis básica para recuperar y imprimir mensajes es:

```python
print(arcpy.GetMessages())
```

Aquí tienes un ejemplo para recuperar los mensajes de la herramienta Clip en un script independiente:

```python
import arcpy
arcpy.env.workspace = "C:/Datos"
infc = "rios.shp"
clipfc = "estudio.shp"
outfc = "resultado.shp"
arcpy.Clip_analysis(infc, clipfc, outfc)
print(arcpy.GetMessages())
```
