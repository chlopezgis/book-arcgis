'''
Autor: Charlie Lopez Rengifo
Fecha: 14/06/2024
Descripción: Crear un buffer a una capa de puntos y luego contar la cantidad
             de registros del resultado
'''

# Import module
import arcpy

# Workspace (data directory)
arcpy.env.workspace = r'D:\Charlie\02_Cursos\02_PROGRAMACION_GIS\ARCPY\Aprendizaje\00-datos'

# overwrite = True
arcpy.env.overwriteOutput = True

# Feature class
fc_cities = 'us_cities'

# geo-processing tools: Buffer (save object Result: path output fc)
buffer = arcpy.Buffer_analysis(fc_cities, 'us_cities_bf', 0.001, dissolve_option='NONE')

# Access geo-processing tools: GetCount (save object Result: integer)
count = arcpy.GetCount_management(buffer)
print(f'Output rows: {count}')

# Message finish process
print('End process')
