#!/bin/bash
RESET="\e[0m"
YELLOW="\e[33m"
GREEN="\e[32m"

if [[ ! -e '/usr/bin/python3.10' ]]; then
    echo -e "${YELLOW}python3.10 not found, pls install it before proceeding${RESET}"
    exit 1
fi

read -p "This script will setup the downloader in the current directory, are you sure? (y/n) " answer

case ${answer} in
    y|yes)
        echo "Ok, let's go!"
        ;;
    n|no)
        echo "Ok, call me when you decide another directory, bye!"
        exit
        ;;
esac

echo -e "First let's clone youtube_dl lib...\n"
/usr/bin/git clone https://github.com/ytdl-org/youtube-dl.git
echo ''

if [[ ${?} != 0 ]]; then
    echo -e "${YELLOW}Something went wrong with the git clone, check it manually pls${RESET}"
    exit 1
fi

echo "Now let's setup the enviornment..."
/usr/bin/python3.10 -m venv .env
if [[ ${?} != 0 ]]; then
    echo -e "${YELLOW}Something went wrong creation of the .env, check it manually pls${RESET}"
    exit 1

    else
    echo "done"
    
fi

mkdir ./.env/lib/python3.10/site-packages/youtube_dl/
rsync -arh ./youtube-dl/youtube_dl/* ./.env/lib/python3.10/site-packages/youtube_dl/

if [[ ${?} == 0 ]]; then
    echo -e "\n${GREEN}All done! you can now download your music from youtube by entering the env by running: 'source .env/bin/activate' (just once)\nthen download your music with: 'python downloader.py \"https://youtube.com/SOMETHING\"'${RESET}"
    echo -e "\n${GREEN}OBS: you can download multiple musics feeding multiple URLs separated by spaces, I recommend using simple quotes to prevent the URLs from doing weird things in the terminal, that's it, have fun!${RESET}"
    exit 0

    else
    echo "${YELLOW}Something went wrong with the youtube_dl setup in the enviornment, please check manually${RESET}"
fi
