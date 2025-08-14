[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
# Cmus discord rich presence
A small python script using pypresence to show cmus status. Song (and current position), album, year, artist, and album art are shown. 

Three files will be created when the script is run. Album art is extracted from the music file to file.jpg and uploaded to [litterbox.catbox.moe](https://litterbox.catbox.moe/), which temporarily stores the file for 2 hours. The link for the uploaded image will be stored in link.txt. Information regarding the song will be stored in the data.txt. 

## To do (a lot 😭):
- [ ] Stop elapsed time when paused (time currently continues)
- [ ] Update time when song is fast fowarded
- [ ] Update time when song is repeated/restarted
- [ ] Set correct elapsed time when script is started when a song is already playing
- [ ] Set default/blank image when file does not have album art tag
- [ ] Allow script to run if cmus is not running, waiting for cmus to run

## Requirements:
- python 3.8 or higher
- ffmpeg: installed using `sudo apt-get install ffmpeg`
- curl: installed using `sudo apt-get install curl`
- pypresence: installed using `pip install pypresence`

## Usage:
Run `python3 rpc.py`. To stop/quit press control-c.

Currently only supported on Linux, as I haven't tested the script on other operating systems. It _might_ work on Mac.

## Example
![Image of a discord rich presence with album art and details](rpc.png)
