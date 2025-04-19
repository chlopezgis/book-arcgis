# **Configuración de un espacio de trabajo**

Configurar un espacio de trabajo en `ArcPy` es una de las primeras tareas que se realizan en un script de geoprocesamiento. Un espacio de trabajo define una **ubicación predeterminada** para las **entradas y salidas** de las herramientas de geoprocesamiento.

A continuación, el siguiente código establece el espacio de trabajo actual en "_C:\Data_"

```python
import arcpy

# Configurar el espacio de trabajo
arcpy.env.workspace = "C:\\Data"
```
