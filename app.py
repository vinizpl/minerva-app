import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Minerva Billboard", page_icon="🎵", layout="wide")

def garantir_csv():
    file_name = "billboard_hot_100.csv"
    if not os.path.exists(file_name):
        dates = pd.date_range(start="2020-01-01", end="2025-12-31", freq="W-SAT")
        pool = [
            ("Blinding Lights", "The Weeknd", "1614613535301-0e28a33a4a33"),
            ("Levitating", "Dua Lipa", "1493225255760-d9525035f63d"),
            ("As It Was", "Harry Styles", "1470225620359-4a09e7e514af"),
            ("Flowers", "Miley Cyrus", "1459749411174-8328f7813635"),
            ("Anti-Hero", "Taylor Swift", "1508700115892-45cd13cc245e"),
            ("Stay", "The Kid LAROI", "1493225255760-d9525035f63d"),
            ("Heat Waves", "Glass Animals", "1526218626217-dc12372398e2"),
            ("Vampire", "Olivia Rodrigo", "1514525253514-1f65596b8a17"),
            ("Cruel Summer", "Taylor Swift", "1459749411174-8328f7813635"),
            ("Starboy", "The Weeknd", "1614613535301-0e28a33a4a33")
        ]
        
        rows = []
        for date in dates:
            np.random.shuffle(pool)
            for rank in range(1, 11):
                title, artist, img_id = pool[rank-1]
                url = f"https://open.spotify.com/search/{title.replace(' ', '%20')}%20{artist.replace(' ', '%20')}"
                img_url = "Imagens/download.png" 
                rows.append([date.strftime('%Y-%m-%d'), title, artist, rank, url, img_url])
        
        df_gen = pd.DataFrame(rows, columns=['date', 'title', 'artist', 'rank', 'spotify_url', 'img_url'])
        df_gen.to_csv(file_name, index=False)
        return df_gen
    return pd.read_csv(file_name)

st.markdown("""
    <style>
    .main { background-color: #121212; }
    .song-card {
        background: #1e1e1e;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        border: 1px solid #333;
    }
    .album-art {
        width: 70px; height: 70px;
        border-radius: 8px; margin-right: 20px;
        object-fit: cover;
    }
    .song-title { font-size: 1.1rem; font-weight: bold; color: white; margin: 0; }
    .artist-name { color: #b3b3b3; }
    .rank-num { color: #1DB954; font-weight: bold; margin-right: 15px; font-size: 1.2rem; }
    .spotify-btn {
        background-color: #1DB954; color: white !important;
        padding: 8px 20px; border-radius: 20px;
        text-decoration: none; font-weight: bold; font-size: 13px;
    }
    </style>
    """, unsafe_allow_html=True)

df = garantir_csv()
df['date'] = pd.to_datetime(df['date'])

# Interface
st.title("🎵 Minerva Hits Billboard")

with st.sidebar:
    st.header("Filtros")
    ano = st.selectbox("Ano", sorted(df['date'].dt.year.unique(), reverse=True))
    mes = st.slider("Mês", 1, 12)

filtered = df[(df['date'].dt.year == ano) & (df['date'].dt.month == mes)]

if not filtered.empty:
    latest_date = filtered['date'].max()
    top_10 = filtered[filtered['date'] == latest_date].sort_values('rank').head(10)
    
    st.subheader(f"Top 10 — {latest_date.strftime('%d/%m/%Y')}")

    for _, row in top_10.iterrows():
        st.markdown(f"""
            <div class="song-card">
                <div class="rank-num">#{row['rank']}</div>
                <img src="{row['img_url']}" class="album-art">
                <div style="flex-grow: 1;">
                    <p class="song-title">{row['title']}</p>
                    <p class="artist-name">{row['artist']}</p>
                </div>
                <a href="{row['spotify_url']}" target="_blank" class="spotify-btn">OUVIR</a>
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("Nenhum dado encontrado para este período.")