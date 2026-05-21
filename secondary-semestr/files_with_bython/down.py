import yt_dlp

url = input("Enter video URL: ")

ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",  
    "merge_output_format": "mp4",
    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": True,

    # Timeout va retry sozlamalari
    "socket_timeout": 60,       # 60 sekund kutadi
    "retries": 10,              # 10 marta qayta urinadi
    "fragment_retries": 10,     # har segment uchun qayta urinish
    "http_chunk_size": 10485760 # 10 MB bo'laklarga bo'lib yuklaydi
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])