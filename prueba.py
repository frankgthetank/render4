import geopandas as gpd

# Ruta al archivo .gpkg de entrada
gpkg_file = "C:\\Users\\anali\\OneDrive\\Documentos\\render2\\sectores_anonimizados 1.gpkg"




# Leer el archivo .gpkg
gdf = gpd.read_file(gpkg_file)

gdf = gdf.to_crs(epsg=4326)

# Ruta al archivo .geojson de salida
geojson_file = "output_filesectores.geojson"

# Guardar como GeoJSON
gdf.to_file(geojson_file, driver="GeoJSON")

print(f"Archivo convertido y guardado en: {geojson_file}")
