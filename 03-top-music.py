# Script para buscar top canciones segun artista / banda y descargarla desde YT

import requests
import subprocess
import os

API_KEY = ""  
URL = "http://ws.audioscrobbler.com/2.0/"

def top_canciones(artista):
    params = {
        "method": "artist.gettoptracks",
        "artist": artista,
        "api_key": API_KEY,
        "format": "json",
        "limit": 7
    }
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()

        tracks = data.get("toptracks", {}).get("track", [])
        if not tracks:
            print("No se encontraron canciones para ese artista.")
            return []

        print(f"\nTop 5 canciones de {artista}:\n")
        canciones = []
        for i, track in enumerate(tracks, start=1):
            nombre = track['name']
            print(f"{i}. {nombre}")
            canciones.append(nombre)
        return canciones

    except Exception as e:
        print("Error al consultar la API:", e)
        return []

def descargar_cancion(artista, titulo):
    query = f"{artista} {titulo}"
    ruta_descargas = os.path.expanduser("~/Downloads")
    os.makedirs(ruta_descargas, exist_ok=True)  

    print(f"\nDescargando: {query}")
    try:
        subprocess.run([
            "yt-dlp",
            f"ytsearch1:{query}",   
            "-x",                  
            "--audio-format", "mp3",
            "-o", f"{ruta_descargas}/{artista} - {titulo}.%(ext)s"
        ])
    except Exception as e:
        print("Error al descargar:", e)

if __name__ == "__main__":
    artista = input("Ingresa el nombre del artista: ")
    canciones = top_canciones(artista)
    for titulo in canciones:
        descargar_cancion(artista, titulo)
