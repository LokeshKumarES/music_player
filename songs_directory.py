import os
import re

def get_song(query=None):
    songs_list = []
    songs_dict = {}
    dir_path = 'songs'
    try:
        songs_list = os.listdir(dir_path)
        
        filter_list = []
        if query:
            pattern = re.compile(re.escape(query), re.IGNORECASE)
            for s_path in songs_list:                
                if pattern.search(s_path):
                    # print(s_path)
                    filter_list.append(s_path)
        if not filter_list:
            filter_list = songs_list.copy()
        
        songs_dict = {s_path : os.path.join(dir_path, s_path) for s_path in filter_list}
    except Exception as e:
        print("Unable to get song/songs!:{e}")
    return songs_dict



