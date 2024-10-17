from pytube import YouTube
import os, re
import traceback


def download_by_url(yt_url=None):
    try:
        if yt_url:
            # Create a YouTube object
            yt = YouTube(yt_url,use_po_token=True)
            # print(yt.streams.get_audio_only().download())
            # Filter audio-only streams and download
        
            audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()
            # print(str(audio_stream.default_filename))
            file_name, ext_name = str(audio_stream.default_filename).rsplit('.',1)
            file_name = re.sub(r'[^\w\s-]', '', file_name).strip()
            file_name = re.sub(r"\s\s+", " ", file_name)
            # print(f"File: {file_name}")
            safe_filename = f"{file_name}.{ext_name}"
            # print("SAFE FILE: ", safe_filename)
            if safe_filename not in os.listdir('songs'):
                print("Not found")
                audio_stream.download(output_path='songs', filename=safe_filename)
            
            return safe_filename
        else:
            return None
    except Exception as e:
        print(f"Error in Downloading music from youtube url: {yt_url}")
        print(traceback.format_exc())
        return None # traceback.format_exc()
    return None

# download_by_url("https://www.youtube.com/watch?v=hOHKltAiKXQ")

