import yt_dlp as youtube_dl
import streamlit as st
import os
from pathlib import Path
import platform


def get_default_download_path():
    """
    Returns the default download path based on the platform.
    """
    system = platform.system().lower()
    
    if system == 'windows':
        return str(Path.home() / 'Downloads')
    
    elif system == 'darwin':  # macOS
        return str(Path.home() / 'Downloads')
    
    elif system == 'linux':
        return str(Path.home() / 'Downloads')
    
    elif system == 'android':
        return str(Path.home() / 'Downloads')  # Handle Android download path
    
    elif system == 'ios':
        return str(Path.home() / 'Downloads')  # Handle iOS download path
    
    else:
        return str(Path.home())


def search_youtube(query):
    """
    Searches YouTube for videos based on the user's query.
    """
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Don't download, just get video metadata
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch:{query}", download=False)
        return result['entries']  # Returns a list of video entries



def download_video(url, save_path, audio_only=False):
    """
    Downloads the video or audio from YouTube and saves it to the specified path.
    This version avoids merging audio and video (no need for ffmpeg).
    """
    try:
        # Set up custom headers and options to download the best video or audio file
        ydl_opts = {
            'format': 'best',  # Download the best single file (no merging)
            'noplaylist': True,  # Ensure it's only downloading a single video
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save video in the specified path
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'  # Updated User-Agent
            },
            'progress_hooks': [progress_hook],  # Add progress hook to update Streamlit progress bar
            'retry': 3,  # Retry the download a few times in case of failure
            'extractaudio': audio_only,  # Extract audio if audio_only is True
        }

        # If the user wants audio only, adjust the format option
        if audio_only:
            ydl_opts['format'] = 'bestaudio/best'  # Download the best audio file only

        # Use yt-dlp to download the video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Show success notification with confetti
        st.success(f"✅ Download completed successfully! The file was saved to {save_path}")
        st.balloons()  # Trigger confetti animation

    except Exception as e:
        st.error(f"Error: {e}")



# Progress hook function to update the Streamlit progress bar
def progress_hook(d):
    try:
        if d['status'] == 'downloading':
            total_size = d.get('total_bytes', None)
            downloaded = d.get('downloaded_bytes', 0)

            if total_size:
                # Ensure the progress value is within a valid range (0.0 to 1.0)
                progress = downloaded / total_size  # Calculate progress as a fraction
                progress = min(1.0, max(0.0, progress))  # Ensure it stays within [0, 1]
                st.progress(progress)  # Update progress bar
            else:
                # If no total size, show the download progress in some estimated range
                progress = downloaded / 1000000  # Arbitrary scale for progress in case no total size is available
                st.progress(min(1.0, max(0.0, progress)))  # Clamp between 0 and 1

    except Exception as e:
        st.error(f"Error in progress hook: {e}")


def main():
    st.set_page_config(page_title="Rhonzkieee", page_icon="📺", layout="centered")
    
    # Add an overview of the app
    st.title("🎬 RhonzTube Downloader 🎧")
    st.write(
        """
        Welcome to **Rhonzkieee**, your ultimate tool for downloading YouTube videos and audio in just a few clicks! 🎉
        
        📹 **What can you do here?**  
        - **Search YouTube:** Enter a video title or link.
        - **Choose your download:** Pick between video or audio format.
        - **Download your favorite content** directly to your device! 🚀
        
        Let's get started! 👇
        """
    )

    # User input for YouTube search query
    query = st.text_input("🔍 Enter YouTube link or search query:", '')

    if query:
        # Search for videos based on the query
        search_results = search_youtube(query)

        if search_results:
            # Display search results in a dropdown menu
            video_options = {f"{entry['title']}": entry['url'] for entry in search_results}
            selected_video = st.selectbox("🎥 Select a video to download:", options=list(video_options.keys()))

            # Option to choose download type (Audio or Video)
            download_option = st.radio("💾 Choose download type:", ('Video', 'Audio'))

            # Get the selected video URL
            video_url = video_options[selected_video]

            # Display the selected video URL
            st.write(f"📹 Selected video: {selected_video}")

            # Get the default download path
            save_dir = get_default_download_path()

            st.write(f"📂 Saving to: {save_dir}")

            # If the user clicks the download button
            if st.button("Download 📥"):
                st.write("🔄 Downloading...")
                audio_only = download_option == 'Audio'
                download_video(video_url, save_dir, audio_only)

        else:
            st.warning("❗ No results found for your query. Please try another search term.")

if __name__ == "__main__":
    main()
