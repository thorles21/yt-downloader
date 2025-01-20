import yt_dlp as youtube_dl
import sys
import os

MUSIC_LOG = './musics/downloaded.log'
VIDEO_LOG = './videos/downloaded.log'

if len(sys.argv) < 2:
    print('Invalid argument, please input a valid URL')
    sys.exit()

video_url = sys.argv[1]

# Options for music download
audio_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': './musics/%(title)s.%(ext)s',
    'fragment_retries': 10,
    'retries': 10,
    'concurrent_fragment_downloads': 5,
    'continuedl': True,
    'nocheckcertificate': True,
}

# Options for video download
video_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': './videos/%(title)s.%(ext)s',
    'fragment_retries': 10,
    'retries': 10,
    'concurrent_fragment_downloads': 5,
    'continuedl': True,
    'nocheckcertificate': True,
}

def log_download(log_file, title):
    with open(log_file, 'a') as log:
        log.write(title + '\n')

def check_log(log_file, title):
    if os.path.exists(log_file):
        with open(log_file, 'r') as log:
            downloads = log.read().splitlines()
        if title in downloads:
            return True
    return False

def download_vid(video_url, download_type='audio'):
    ydl_opts = audio_opts if download_type == 'audio' else video_opts
    log_file = MUSIC_LOG if download_type == 'audio' else VIDEO_LOG

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', None)

            if video_title:
                if check_log(log_file, video_title):
                    confirm = input(f'"{video_title}" already downloaded. Download again? (y/n): ')
                    if confirm.lower() != 'y':
                        print(f'Skipping "{video_title}"')
                        return

                print(f'Downloading "{video_title}"')
                ydl.download([video_url])
                print(f"Finished '{video_title}' download ")
                log_download(log_file, video_title)
            else:
                print("Could not retrieve video title")
    except KeyboardInterrupt:
        print('Download canceled by user')
    except Exception as e:
        print(f'Error: {e}')

for arg in sys.argv[1:]:
    if '--video' in sys.argv:
        download_vid(video_url=arg, download_type='video')
    else:
        download_vid(video_url=arg)