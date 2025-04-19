'''
Autor: Charlie Lopez Rengifo
Fecha: 18/06/2024
Descripción: Obtener el CRS de una capa utilizando diferentes métodos
'''

# Import module
import arcpy
import os

# 1. Workspace
path = r'D:\Charlie\02_Cursos\02_PROGRAMACION_GIS\ARCPY\Aprendizaje\00-datos'

# 2. Input FC
data = 'Precip2008Readings.shp'

# 3. Describe CRS of the input
desc = arcpy.Describe(os.path.join(path, data))
print(desc.name)
print(desc.dataType)
print(desc.shapeType)
# Obtain CRS
print(desc.spatialReference.name)

# 4. Obtain CRS using name
sr = arcpy.SpatialReference("NAD 1983 StatePlane Texas Central FIPS 4203 (US Feet)")
print(sr.name)

# 5. Obtain CRS using EPSG (WKID)
sr = arcpy.SpatialReference(32718)
print(sr.name)
print(sr.type)
print(sr.linearUnitName)
