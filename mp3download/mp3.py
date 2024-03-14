import os
import pandas as pd
from pytube import YouTube
from moviepy.editor import *

# CSV dosyasından video linklerini oku
csv_file = "yeniveriseti.csv"
df = pd.read_csv(csv_file)

# Klasör oluştur (varsa tekrar oluşturmayacak)
output_folder = "mp3"
os.makedirs(output_folder, exist_ok=True)

# Her bir video linki için dönüştürme işlemini uygula
for index, row in df.iterrows():
    try:
        link = row['YouTube Link']
        track_name = row['Track Name']  # track name sütunundan ismi al
        # YouTube video nesnesini oluştur
        yt = YouTube(link)

        # Videoyu en yüksek çözünürlükte indir
        print("Video indiriliyor:", link)
        video_path = yt.streams.get_highest_resolution().download()

        # Videoyu MP3 formatına dönüştür
        print("Video MP3 formatına dönüştürülüyor...")
        video = VideoFileClip(video_path)
        audio_path = os.path.join(output_folder, f"{track_name}.mp3")  # MP3 dosyasını "mp3" klasörü altında sakla
        video.audio.write_audiofile(audio_path)
        
        # İndirilen video dosyasını sil
        video.close()
        os.remove(video_path)

        print("Video MP3 formatına başarıyla dönüştürüldü:", audio_path)
    except Exception as e:
        print(f"Hata oluştu: {e}")

print("Tüm videolar dönüştürüldü ve MP3 dosyaları 'mp3' klasöründe saklandı.")