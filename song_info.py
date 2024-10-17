from mutagen import File
import traceback
import os


def get_info(file_path=None):
    try:
        data = {

        }
        file_name = os.path.basename(file_path)
        # Load the audio file
        audio = File(file_path)

        # Display audio information
        # print(f"Audio Info for: {file_path}")
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path) / (1024*1024)
        data = {
                "title": file_name,
                "size": f"{round(file_size, 2)} MB"
        }

        if audio:
            '''
            print(f"File Size: {round(file_size, 2)} MB")
            print(f"Length: {round(audio.info.length/60, 2)} Minutes")
            print(f"Bitrate: {audio.info.bitrate} bps")
            print(f"Channels: {audio.info.channels}")
            print(f"Sample Rate: {audio.info.sample_rate} Hz")
            '''
            data_1 = {
                "title": file_name,
                "size": f"{round(file_size, 2)} MB",
                "duration": f"{round(audio.info.length/60, 2)} Minutes",
                "bitrate": f"{audio.info.bitrate} bps",
                "channels": audio.info.channels,
                "sample_rate": f"{audio.info.sample_rate} Hz"
            }
            data.update(data_1)
            
        else:
            print("Could not retrieve audio info.")

       
    except Exception as e:
        print(f"Error in extracting info from audio file: {file_path}")
        print(f"Error: {traceback.format_exc()}")
    return data

get_info(r"songs\Todh.mp3")
