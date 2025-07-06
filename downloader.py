import subprocess
import os

def download_video(url, output_dir='downloads'):
    os.makedirs(output_dir, exist_ok=True)
    print(f"📥 Downloading from: {url}")
    command = [
        'yt-dlp',
        '-f', 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        '--merge-output-format', 'mp4',
        '-o', f'{output_dir}/%(title).80s.%(ext)s',
        url
    ]
    subprocess.run(command)
