
import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

# --- Configuración inicial ---
st.set_page_config(page_title="Riesgo de Inundación", layout="centered")

st.title("🌧️ Mapa de Riesgo de Inundaciones - Longchamps")
st.markdown("Consulta el clima actual y las zonas marcadas como riesgosas.")

# --- Coordenadas de Longchamps ---
lat = -34.8382
lon = -58.3853

# --- API de OpenWeatherMap ---
API_KEY = "339ab770edb82abe8f80f5376d863304"

def obtener_clima(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=es"
    r = requests.get(url)
    if r.status_code == 200:
        datos = r.json()
        clima = datos["weather"][0]["description"].capitalize()
        temp = datos["main"]["temp"]
        return f"{clima}, {temp} °C"
    else:
        return "No se pudo obtener el clima."

# --- Obtener clima actual ---
clima = obtener_clima(lat, lon, API_KEY)

# --- Crear el mapa con Folium ---
m = folium.Map(location=[lat, lon], zoom_start=16)
folium.Marker(
    location=[lat, lon],
    popup=f"Zona de riesgo\nClima: {clima}",
    tooltip="Carlos Bunge",
    icon=folium.Icon(color="red", icon="cloud")
).add_to(m)

# --- Mostrar el mapa en Streamlit ---
st_data = st_folium(m, width=700, height=500)
