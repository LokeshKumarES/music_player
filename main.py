import streamlit as st
from streamlit_option_menu import option_menu
import os
from songs_directory import get_song, get_file_path
from yt_downloader import download_by_url
from song_info import get_info

# Title of the app
st.set_page_config(page_title='🎶 Player 🎶', layout="wide")

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0)
    
    uploaded_files = st.file_uploader("", accept_multiple_files=True, label_visibility="hidden")
    if uploaded_files is not None:
        if len(uploaded_files)>0:
            for uploaded_file in uploaded_files:
                #st.info(upload_file.name)
                save_path = get_file_path(str(uploaded_file.name))
                if not os.path.exists(save_path):
                    with open(save_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                else:
                    st.warning(f"File Already Exists!: {uploaded_file.name}")
            
            st.success(f"{len(uploaded_files)} File Uploaded successfully!")


    # st.text_input("", placeholder="Enter Youtube URL", key="yt_url", label_visibility="hidden")
    # if st.button("Search"):
    #     yt_url = st.session_state.get('yt_url')
    #     if yt_url:
    #         print('yt_url: ', yt_url)
    #         curr_song = download_by_url(yt_url)
    #         st.info(curr_song)
    #         if curr_song:
    #             pass
    #             #st.session_state['curr_song'] = curr_song
    #             #st.session_state['songs_dict'].update({curr_song: os.path.join('songs', curr_song)}) 
            
    #         else:
    #             st.warning("Unable to download music from youtube URL") 
    #     else:
    #         st.warning("Please enter valid youtube URL")



if selected == 'Home':

    st.session_state['songs_dict'] = get_song()
    if st.selectbox("", options=st.session_state.get('songs_dict').keys(), key="curr_song", label_visibility="hidden"):
        audio_path = st.session_state.get('songs_dict').get(st.session_state.get('curr_song'))
        st.audio(audio_path, format="audio/mp3")
        # st.dataframe(get_info(audio_path), use_container_width=True)

if selected == 'Settings':
    st.info("Coming Soon!")

