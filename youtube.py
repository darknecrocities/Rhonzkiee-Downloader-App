import yt_dlp
import streamlit as st
import os

# Function to download video
def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Output file name
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return "Video downloaded successfully!"
    except Exception as e:
        return f"Error: {e}"

# Streamlit interface
def main():
    st.title("YouTube Video Downloader")

    # User input for YouTube URL
    video_url = st.text_input("Enter YouTube Video URL:")

    # Folder picker for saving video
    save_dir = st.text_input("Enter the directory to save video:", value=os.getcwd())

    if st.button("Download Video"):
        if video_url and save_dir:
            with st.spinner("Downloading video..."):
                message = download_video(video_url, save_dir)
                st.success(message)
        else:
            st.error("Please provide both YouTube URL and save directory.")

if __name__ == "__main__":
    main()
