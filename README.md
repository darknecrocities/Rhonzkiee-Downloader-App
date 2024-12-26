
# 🎬 Automation RhonzTube Downloader 🎧

Welcome to **RhonzTube**, your ultimate tool for downloading YouTube videos and audio with just a few clicks! 🚀

## Features 🌟

- **Search YouTube**: Enter a video title or YouTube link and find content instantly! 🔍
- **Choose your download**: Download videos or audio in your preferred format. 🎥🎧
- **Easy Download**: Download your favorite content directly to your device. 📥

## How to Use 📝

1. **Enter a YouTube Link or Search Query**:  
   - Type a video title or a YouTube URL in the input box.  
   - Click on the "Search" button to find matching results.

2. **Select a Video**:  
   - Choose from the displayed search results.

3. **Choose Download Type**:  
   - Select whether you want to download the **video** or just the **audio**.

4. **Download the Content**:  
   - Hit the **Download** button to save your content to your device! 💾

## Technologies Used 🔧

- **Python**: For the core logic and handling YouTube downloads.
- **yt-dlp**: A YouTube video downloader library to fetch videos and audio.
- **Streamlit**: A fast app framework to build the user interface.
- **platform**: For detecting the system and choosing the correct default download path.


## Installation 💻

1. **Clone the repository** or **download the project files**.

2. **Install the necessary dependencies**:
   ```bash
   pip install yt-dlp streamlit
   ```

3. **Run the app**:
   ```bash
   streamlit run main.py
   ```
   
   **Alternatively**, if you prefer to run the app locally or experience the actual application behavior, it's recommended to use `youtube.py`:
   ```bash
   streamlit run youtube.py
   ```

4. **Access the app in your browser**:  
   - Visit `http://localhost:8501` to use the **Rhonzkieee** YouTube downloader.

---

## Notes 📢

- The **default download path** is determined based on your operating system:  
  - **Windows**, **macOS**, **Linux**, **Android**, and **iOS** all default to the `Downloads` folder.

- You can easily download videos or extract audio with the click of a button. 🎶

- **Streamlit** shows a progress bar during downloads to let you track your progress. ⏳

- **Compatible platforms**: iOS, macOS, Linux, Windows, Android, MI.

- **Important**: 
  - If you're downloading audio from YouTube, it might be saved in the `.webm` format, which can be blocked by certain systems due to unsupported cookies. 
  - In such cases, **running `youtube.py` locally** is recommended for proper functionality, as it will download audio in **MP3** format instead.


---

Thank you for using **RhonzTube**! Enjoy downloading your favorite content effortlessly! 🎉

