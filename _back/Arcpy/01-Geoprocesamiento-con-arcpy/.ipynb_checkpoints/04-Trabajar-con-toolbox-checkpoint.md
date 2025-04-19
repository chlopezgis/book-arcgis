# **Trabajar con cajas de herramientas en ArcPy**

## **Importar una caja de herramientas personalizada**

Para acceder a las herramientas almacenadas en una **caja de herramientas personalizada**, es necesario importarla usando **`arcpy.ImportToolbox()`**. Esta función se refiere al archivo ".tbx" en el disco, no al nombre de la caja de herramientas. Si no se define un alias para la caja de herramientas, se puede **establecer un alias temporal al importarla**:

```python
arcpy.ImportToolbox("C:/Data/sampletools.tbx", "mytools")
```

Donde:

* **`"C:/Data/sampletools.tbx"`**: Ruta completa del archivo ".tbx" en el disco.
* **`mytools`**: Alias para la caja de herramientas.

## **Acceder a una herramienta personalizada**

La sintaxis para acceder a una herramienta importada es la misma que para acceder a herramientas de las cajas de herramientas del sistema:

```python
arcpy.<toolname>_<toolboxalias>(<parámetros>)
```

Donde:

* **`toolname`**: Nombre de la herramienta dentro de la caja de herramientas importada.
* **`toolboxalias`**: Alias de la caja de herramientas.
* **`parámetros`**: Parámetros de la herramienta

**Ejemplo:**

Si el archivo **"C:/Data/sampletools.tbx"** contiene una herramienta llamada **MyModel**, la sintaxis para acceder a esta herramienta es:

```python
# como funcion
arcpy.MyModel_mytools(<parámetros>)

# o como modulo
arcpy.mytools.MyModel(<parámetros>)
```

>**NOTA**: `ImportToolbox()` también puede añadir servicios de geoprocesamiento desde servidores locales o de internet.
