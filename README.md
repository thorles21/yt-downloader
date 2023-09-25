# yt-downloader
python utility to download music from yt (I'm using ubuntu, so this hasn't been tested in any other enviornment)

Installation:

Clone the repo
- run installer.sh
- enjoy!

Usage:
- Activate the virtual enviorment by running: 'source .env/bin/activate'
- Run "python downloader.py 'https://youtube.com/something' 'https://youtube.com/something-else' ..."

  You can download one or more videos by feeding the URL in the command line, the audio will be saved in mp3 (or webm if you do not have ffmpeg or ffprobe installed) in the ./music/ folder in the same directory your script is installed.
