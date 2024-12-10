import requests
import geopandas as gpd
import json
from dash import Dash, html
import dash_leaflet as dl
from io import BytesIO
import pyproj

# URL del archivo GeoJSON en Google Drive
GEOJSON_URL = "https://drive.google.com/uc?id=1HkHBBb5chWjcua97xS-xqvx4OCX5Ijq0&export=download"

#nuevo   https://drive.google.com/file/d/1HkHBBb5chWjcua97xS-xqvx4OCX5Ijq0/view?usp=sharing
#https://drive.google.com/file/d/1FLDh0D9UKmHTkzw6asKzfpRFDxSU8wC-/view?usp=sharing

def fetch_geojson(url):
    """
    Descarga el archivo GeoJSON desde una URL y lo carga como GeoJSON.
    """
    response = requests.get(url)
    if response.status_code == 200:
        # Cargar el archivo en un GeoDataFrame
        gdf = gpd.read_file(BytesIO(response.content))
        # Convertir a GeoJSON
        return json.loads(gdf.to_json())
    else:
        raise Exception(f"No se pudo descargar el archivo: {response.status_code}")

# Descargar los datos GeoJSON
geojson_data = fetch_geojson(GEOJSON_URL)

#print(geojson_data.getheaders())



# Crear la aplicación Dash
app = Dash(__name__)

# Diseño de la aplicación
app.layout = html.Div([
    dl.Map([
        dl.TileLayer(),  # Capa base
        dl.GeoJSON(data=geojson_data,  # Capa GeoJSON
                   options={"style": {"color": "blue", "weight": 2}},
                   id="geojson-layer"),
    ], style={'width': '100%', 'height': '500px'}, center=(0, 0), zoom=2)
])

# Servidor de la aplicación (necesario para Render)
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)





