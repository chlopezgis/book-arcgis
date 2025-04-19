# **Parámetros de las herramientas de geoprocesamiento**

Cada herramienta de geoprocesamiento tiene parámetros, incluidos los **`obligatorios`** y **`opcionales`**, que proporcionan a la herramienta la información que necesita para ejecutarse.

>La documentación de cada herramienta en ArcGIS Pro ayuda a describir sus parámetros y propiedades.

## Sintaxis

La sintaxis de las herramientas de geoprocesamiento en ArcPy sigue un patrón común que facilita la especificación de los parámetros requeridos para ejecutar la herramienta de manera correcta. Un ejemplo de la sintaxis completa de una herramienta de geoprocesamiento en ArcPy sería:

```python
Nombre_de_la_Herramienta(parámetro_obligatorio1,
                         parámetro_obligatorio2, ...,
                         {parámetro_opcional1},
                         {parámetro_opcional2},
                         ...)
```

Donde

* **`Nombre_de_la_herramienta`**: Se utiliza para invocar la función que representa esa herramienta en ArcPy.

* **`Parámetros_obligatorios`**: Son aquellos que **deben proporcionarse para que la herramienta se ejecute correctamente**. Estos parámetros suelen ser los conjuntos de datos de entrada y salida necesarios para realizar la operación de geoprocesamiento.

* **`Parámetros_opcionales`**: Son aquellos que **no son estrictamente necesarios para ejecutar la herramienta**, pero pueden ajustar o controlar su comportamiento. Estos parámetros suelen estar encerrados entre llaves {} para indicar que son opcionales.

>**NOTA**: Los parámetros deben ser introducidos siguiendo el orden indicado por la herramienta. En caso de introducirlos en un orden incorrecto, se debe especificar el nombre del parámetro junto con su respectivo valor, siguiendo el formato: ___nombre_parametro=valor___

## Manejo de Parámetros Opcionales

En ArcPy, los parámetros opcionales pueden manejarse de las siguientes maneras:

**1. Usar cadenas vacías, numeral o valores nulos**

Utilizar cadenas vacías (_""_), numeral (_"#"_) o valores nulos (_None_) para indicar que no se proporciona ningún valor para un parámetro opcional:


```python
# Cadenas vacías ""
arcpy.Buffer_analysis("roads", "buffer", "100 METERS", "", "", "LIST", "CODE")

# Numeral "#"
arcpy.Buffer_analysis("roads", "buffer", "100 METERS", "#", "#", "LIST", "CODE")

# Valores nulos None
arcpy.Buffer_analysis("roads", "buffer", "100 METERS", None, None, "LIST", "CODE")
```

**3. Especificar los parámetros por nombre**

Especificar solo los parámetros que deseas establecer por su nombre, omitiendo los demás. Esto permite un código más claro y explícito. Por ejemplo:

```python
arcpy.Buffer_analysis("roads", "buffer", "100 METERS", dissolve_option="LIST", dissolve_field="CODE")
```
