import asyncio import os import sys from downloader import download_video from uploader import upload_video

def read_links(file_path): with open(file_path, 'r') as f: return [line.strip() for line in f if line.strip().startswith('http')]

def get_latest_video(path='downloads'): files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp4')] return max(files, key=os.path.getctime) if files else None

if name == "main": if len(sys.argv) != 2: print("❌ Usage: python contentx.py links.txt") sys.exit(1)

links = read_links(sys.argv[1])

for link in links:
    print(f"\n🔗 Processing: {link}")
    download_video(link)

    latest_video = get_latest_video()
    if latest_video:
        asyncio.run(upload_video(latest_video))
    else:
        print("⚠️ No video found for upload.")

