import re
import unicodedata
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def normalize_title(title):
    title = title.lower()
    replacements = {
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u'
    }
    for k,v in replacements.items():
        title = title.replace(k, v)

    title = unicodedata.normalize('NFD', title).encode('ascii', 'ignore').decode('utf-8')
    title = re.sub(r'[^a-z0-9\s]', '', title)
    title = re.sub(r'\s+', '_', title).strip('_')
    return title

def get_video_title(video_url):
    try:
        r = requests.get(video_url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            meta_title = soup.find("meta", property="og:title")
            if meta_title and meta_title.get("content"):
                return meta_title["content"]
    except:
        pass
    return None

def get_video_id(video_url):
    match = re.search(r'v=([0-9A-Za-z_-]+)', video_url)
    if match:
        return match.group(1)
    return None

def download_transcript():
    status_label.config(text="")  # Yeni link durumunda status temizlenir
    video_url = entry.get().strip()
    if not video_url:
        messagebox.showwarning("Uyarı", "Lütfen bir YouTube linki girin.")
        return

    video_id = get_video_id(video_url)
    if not video_id:
        messagebox.showwarning("Uyarı", "Video ID bulunamadı. Geçerli bir YouTube linki girin.")
        return

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['tr', 'en'])
    except:
        messagebox.showerror("Hata", "Altyazı bulunamadı veya çekilemedi.")
        return

    raw_title = get_video_title(video_url)
    if not raw_title:
        raw_title = video_id

    normalized_title = normalize_title(raw_title)
    today_str = datetime.now().strftime("%Y%m%d")
    filename = f"{today_str}_{normalized_title}.txt"

    text_content = "\n".join([x['text'] for x in transcript])
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text_content)

    status_label.config(text=f"İndirildi: {filename}")

def clear_status(event):
    status_label.config(text="")

root = tk.Tk()
root.title("YouTube Altyazı İndirici")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky="nsew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

entry_label = ttk.Label(frame, text="Video linkini yazın:")
entry_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry = ttk.Entry(frame, width=50)
entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
entry.bind("<Key>", clear_status)

download_button = ttk.Button(frame, text="Metni İndir", command=download_transcript)
download_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")

status_label = ttk.Label(frame, text="", foreground="green")
status_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="w")

root.mainloop()
