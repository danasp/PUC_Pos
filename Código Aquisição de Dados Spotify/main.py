#Tracks Top 50 Global

import datetime
import os
from datetime import date
from os import name
import spotipy
import json
import csv
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

# Arquivo JSON com as credenciais da API do Spotify
with open("C:/Users/danie/OneDrive/Documentos/GitHub/PUC_Pos/Código Aquisição de Dados Spotify/credentials.json", "r", encoding="utf-8") as f:
    credentials = json.load(f)

# Criar um objeto para acessar a API do Spotify
client = SpotifyClientCredentials(client_id=credentials["client_id"],
                                  client_secret=credentials["client_secret"])
sp = spotipy.Spotify(client_credentials_manager=client)

# Extração da playlist do Spotify
playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
playlist = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

# Pegar a data atual
current_date = datetime.date.today().strftime("%Y-%m-%d")

# Criação dos field names para o arquivo CSV
field_names_tab_fact = ["artist_uri",
                        "track_uri",
                        "track_name",
                        "track_pop",
                        "track_album",
                        "release_date",
                        "track_duration_ms",
                        "track_key",
                        "track_bpm",
                        "track_dance",
                        "track_energy",
                        "track_valence",
                        "track_loudness",
                        "track_speechiness",
                        "track_acousticness",
                        "track_instrumentalness",
                        "artist_name",
                        "artist_pop",
                        "artist_genres",
                        "followers",
                        "artist_image",
                        "ranking",
                        "region",
                        "acquisition_date",]

ranking = 0
region = "Global"

# Create the file name with the current date
new_directory = "C:/Users/danie/OneDrive/Documentos/GitHub/PUC_Pos/Dados Spotify/Tabela_Fato"
file_name_tab_fact = f"table_fact_top50_Global_{current_date}.csv"

# Criação da tabela fato
with open(os.path.join(new_directory, file_name_tab_fact), 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names_tab_fact)
    writer.writeheader()  # Write the header row

    for track in sp.playlist_tracks(playlist_URI)["items"]:
        #URI
        track_uri = track["track"]["uri"]
        artist_uri = track["track"]["artists"][0]["uri"]

        #Information
        artist_info = sp.artist(artist_uri)
        features = sp.audio_features(track_uri)[0]

        #Track Data
        track_name = track["track"]["name"]
        track_pop = track["track"]["popularity"]
        album = track["track"]["album"]["name"]
        release_date = track["track"]["album"]['release_date']
        track_duration_ms = features['duration_ms']
        track_key = features['key']
        track_bpm = features['tempo']
        track_dance = features['danceability']
        track_energy = features['energy']
        track_valence = features['valence']
        track_loudness = features['loudness']
        track_speechiness = features['speechiness']
        track_acousticness = features['acousticness']
        track_liveness = features['liveness']
        track_instrumentalness = features['instrumentalness']

        #Artist Data
        artist_name = track["track"]["artists"][0]["name"]
        artist_pop = artist_info["popularity"]
        artist_genres = artist_info["genres"]
        artist_followers = artist_info["followers"]["total"]
        artist_image = artist_info["images"][0]['url']


        #Escrita no arquivo
        ranking = ranking + 1
        track_info = {
            "artist_uri": artist_uri,
            "track_uri": track_uri,
            "track_name": track_name,
            "track_pop": track_pop,
            "track_album": album,
            "release_date": release_date,
            "track_duration_ms": track_duration_ms,
            "track_key": track_key,
            "track_bpm": track_bpm,
            "track_dance": track_dance,
            "track_energy": track_energy,
            "track_valence": track_valence,
            "track_loudness": track_loudness,
            "track_speechiness": track_speechiness,
            "track_acousticness": track_acousticness,
            "track_instrumentalness": track_instrumentalness,
            "artist_name": artist_name,
            "artist_pop": artist_pop,
            "artist_genres": artist_genres,
            "followers": artist_followers,
            "artist_image": artist_image,
            "ranking": ranking,
            "region": region,
            "acquisition_date": current_date,

        }
        writer.writerow(track_info)

#Tracks Top 50 Brasil

# Extração da playlist do Spotify
playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMXbN3EUUhlg?si=aa94b243d7e84402"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
playlist = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

# Pegar a data atual
current_date = datetime.date.today().strftime("%Y-%m-%d")

# Criação dos field names para o arquivo CSV
field_names_tab_fact = ["artist_uri",
                        "track_uri",
                        "track_name",
                        "track_pop",
                        "track_album",
                        "release_date",
                        "track_duration_ms",
                        "track_key",
                        "track_bpm",
                        "track_dance",
                        "track_energy",
                        "track_valence",
                        "track_loudness",
                        "track_speechiness",
                        "track_acousticness",
                        "track_instrumentalness",
                        "artist_name",
                        "artist_pop",
                        "artist_genres",
                        "followers",
                        "artist_image",
                        "ranking",
                        "region",
                        "acquisition_date",]

ranking = 0
region = "Brasil"

# Create the file name with the current date
new_directory = "C:/Users/danie/OneDrive/Documentos/GitHub/PUC_Pos/Dados Spotify/Tabela_Fato"
file_name_tab_fact = f"table_fact_top50_Brasil_{current_date}.csv"

# Criação da tabela fato
with open(os.path.join(new_directory, file_name_tab_fact), 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names_tab_fact)
    writer.writeheader()  # Write the header row

    for track in sp.playlist_tracks(playlist_URI)["items"]:
        #URI
        track_uri = track["track"]["uri"]
        artist_uri = track["track"]["artists"][0]["uri"]

        #Information
        artist_info = sp.artist(artist_uri)
        features = sp.audio_features(track_uri)[0]

        #Track Data
        track_name = track["track"]["name"]
        track_pop = track["track"]["popularity"]
        album = track["track"]["album"]["name"]
        release_date = track["track"]["album"]['release_date']
        track_duration_ms = features['duration_ms']
        track_key = features['key']
        track_bpm = features['tempo']
        track_dance = features['danceability']
        track_energy = features['energy']
        track_valence = features['valence']
        track_loudness = features['loudness']
        track_speechiness = features['speechiness']
        track_acousticness = features['acousticness']
        track_liveness = features['liveness']
        track_instrumentalness = features['instrumentalness']

        #Artist Data
        artist_name = track["track"]["artists"][0]["name"]
        artist_pop = artist_info["popularity"]
        artist_genres = artist_info["genres"]
        artist_followers = artist_info["followers"]["total"]
        artist_image = artist_info["images"][0]['url']


        #Escrita no arquivo
        ranking = ranking + 1
        track_info = {
            "artist_uri": artist_uri,
            "track_uri": track_uri,
            "track_name": track_name,
            "track_pop": track_pop,
            "track_album": album,
            "release_date": release_date,
            "track_duration_ms": track_duration_ms,
            "track_key": track_key,
            "track_bpm": track_bpm,
            "track_dance": track_dance,
            "track_energy": track_energy,
            "track_valence": track_valence,
            "track_loudness": track_loudness,
            "track_speechiness": track_speechiness,
            "track_acousticness": track_acousticness,
            "track_instrumentalness": track_instrumentalness,
            "artist_name": artist_name,
            "artist_pop": artist_pop,
            "artist_genres": artist_genres,
            "followers": artist_followers,
            "artist_image": artist_image,
            "ranking": ranking,
            "region": region,
            "acquisition_date": current_date,

        }
        writer.writerow(track_info)

#Tracks Top 50 USA

# Extração da playlist do Spotify
playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp?si=d26e6e0880dc4d54"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
playlist = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

# Pegar a data atual
current_date = datetime.date.today().strftime("%Y-%m-%d")

# Criação dos field names para o arquivo CSV
field_names_tab_fact = ["artist_uri",
                        "track_uri",
                        "track_name",
                        "track_pop",
                        "track_album",
                        "release_date",
                        "track_duration_ms",
                        "track_key",
                        "track_bpm",
                        "track_dance",
                        "track_energy",
                        "track_valence",
                        "track_loudness",
                        "track_speechiness",
                        "track_acousticness",
                        "track_instrumentalness",
                        "artist_name",
                        "artist_pop",
                        "artist_genres",
                        "followers",
                        "artist_image",
                        "ranking",
                        "region",
                        "acquisition_date",]

ranking = 0
region = "USA"

# Create the file name with the current date
new_directory = "C:/Users/danie/OneDrive/Documentos/GitHub/PUC_Pos/Dados Spotify/Tabela_Fato"
file_name_tab_fact = f"table_fact_top50_USA_{current_date}.csv"

# Criação da tabela fato
with open(os.path.join(new_directory, file_name_tab_fact), 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names_tab_fact)
    writer.writeheader()  # Write the header row

    for track in sp.playlist_tracks(playlist_URI)["items"]:
        #URI
        track_uri = track["track"]["uri"]
        artist_uri = track["track"]["artists"][0]["uri"]

        #Information
        artist_info = sp.artist(artist_uri)
        features = sp.audio_features(track_uri)[0]

        #Track Data
        track_name = track["track"]["name"]
        track_pop = track["track"]["popularity"]
        album = track["track"]["album"]["name"]
        release_date = track["track"]["album"]['release_date']
        track_duration_ms = features['duration_ms']
        track_key = features['key']
        track_bpm = features['tempo']
        track_dance = features['danceability']
        track_energy = features['energy']
        track_valence = features['valence']
        track_loudness = features['loudness']
        track_speechiness = features['speechiness']
        track_acousticness = features['acousticness']
        track_liveness = features['liveness']
        track_instrumentalness = features['instrumentalness']

        #Artist Data
        artist_name = track["track"]["artists"][0]["name"]
        artist_pop = artist_info["popularity"]
        artist_genres = artist_info["genres"]
        artist_followers = artist_info["followers"]["total"]
        artist_image = artist_info["images"][0]['url']


        #Escrita no arquivo
        ranking = ranking + 1
        track_info = {
            "artist_uri": artist_uri,
            "track_uri": track_uri,
            "track_name": track_name,
            "track_pop": track_pop,
            "track_album": album,
            "release_date": release_date,
            "track_duration_ms": track_duration_ms,
            "track_key": track_key,
            "track_bpm": track_bpm,
            "track_dance": track_dance,
            "track_energy": track_energy,
            "track_valence": track_valence,
            "track_loudness": track_loudness,
            "track_speechiness": track_speechiness,
            "track_acousticness": track_acousticness,
            "track_instrumentalness": track_instrumentalness,
            "artist_name": artist_name,
            "artist_pop": artist_pop,
            "artist_genres": artist_genres,
            "followers": artist_followers,
            "artist_image": artist_image,
            "ranking": ranking,
            "region": region,
            "acquisition_date": current_date,

        }
        writer.writerow(track_info)