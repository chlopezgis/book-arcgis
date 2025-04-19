'''
Autor: Charlie Lopez
Fecha: 31/05/2024
Descripcion: Script para reproyectar todos los archivos de un directorio desde el
             CRS 4326 al que indique el usuario
'''

# 1. Importar los modulos
import arcpy
import os

# 2. Configuración de parametros
dirIn = arcpy.GetParameterAsText(0)  # directorio de entrada de data
dirOu = arcpy.GetParameterAsText(1)  # directorio de salida de data
outCRS = arcpy.GetParameter(2)       # Sistema de referencia de salida
pref = arcpy.GetParameterAsText(3)   # Prefijo de la capa de salida

# 3. Geoprocesamiento: Proyectar las capas  de EPSG:4326 a ...
# Listar los shapefiles del directorio de entrada
list_in_project = [file for file in os.listdir(dirIn) if '.shp' in file]
# Configurar los archivos de salida
list_out_project = [str(pref) + file for file in list_in_project]
# Projectar de WGS 84 a outCRS
for in_feat, out_feat in zip(list_in_project, list_out_project):
    fileIn = os.path.join(dirIn, in_feat)            # Concatenar directorio de entrada + shpIn
    fileOu = os.path.join(dirOu, out_feat)           # Concatenar directorio de salida + shapefile
    arcpy.Project_management(fileIn, fileOu, outCRS) # Proyecion