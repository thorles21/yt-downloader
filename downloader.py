import youtube_dl
import sys

if len(sys.argv) < 2:
    errmsg = f'Invalid argument, please input a valid URL'
    print(errmsg)
    sys.exit()

video_url = sys.argv[1]

#Options
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': './musics/%(title)s.%(ext)s',
}

def download_vid(video_url):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', None)

            if video_title:
                print(f'Downloading "{video_title}"')
                ydl.download([video_url])
                print(f"Finished '{video_title}' download ")
            else:
                print("Could not retrieve video title")
    except KeyboardInterrupt as err:
        print(f'Download canceled by user')


for arg in sys.argv:
    if arg == sys.argv[0]:
        continue
    download_vid(video_url=arg)
