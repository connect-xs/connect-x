import os
import time
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
channel_id = os.getenv("CHANNEL_ID")

client = TelegramClient('session', api_id, api_hash)

async def upload_video(video_path):
    await client.start()

    file_size = os.path.getsize(video_path)
    start_time = time.time()
    entity = await client.get_entity(channel_id)

    print(f"🚀 Uploading {os.path.basename(video_path)} ({file_size / (1024*1024):.2f} MB)")

    async def progress_callback(current, total):
        elapsed = time.time() - start_time
        speed = current / elapsed if elapsed > 0 else 0
        percent = (current / total) * 100
        print(f\"\\rUploading: {percent:.2f}% | {speed / (1024 * 1024):.2f} MB/s\", end=\"\")

    await client.send_file(
        entity=entity,
        file=video_path,
        caption=\"🎥 Uploaded by Content-x\",
        progress_callback=progress_callback,
        supports_streaming=True
    )

    print(\"\\n✅ Upload complete!\")
    os.remove(video_path)
    print(f\"🧹 Deleted: {video_path}\")
