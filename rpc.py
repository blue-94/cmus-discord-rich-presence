from pypresence import Presence
import io
from math import floor
import time
import os

# unit in time in which the program runs
TIME = 1
client_id = '1288192736528306310'
artist = ""
song = ""
album = ""
cover = ""
link = ""

# start rich presence
RPC = Presence(client_id, pipe=0)
RPC.connect()

# while program runs update status every TIME seconds
while True:
    change = False
    os.system("cmus-remote -Q > data.txt")
    f = open("data.txt", "r")
    lines = f.readlines()
    #checkDifferentSong(RPC, song, artist)

    # assign needed parts form cmus-remote -Q that we need
    if song != lines[6][9:]:
        song = lines[6][9:]
        file = str(lines[1][5:])
        
        start_time = int(time.time())
        #end_time = start_time + (int(lines[2][8:]) - int(lines[3][8:]))

        if artist != lines[4][10:]:
            artist = lines[4][10:]
        
        change = True

    if album != lines[5][9:]:
        album = lines[5][9:]

        if lines[8][0:16] == "tag originaldate":
            year = lines[8][16:]
        else:
            year = lines[7][8:]

        os.system('ffmpeg -i "' + lines[1][5:-1] + '" -an -c:v copy file.jpg -y -hide_banner -loglevel error')
        os.system('curl -s -F "reqtype=fileupload" -F "time=1h" -F "fileToUpload=@file.jpg" https://litterbox.catbox.moe/resources/internals/api.php > link.txt')
        
        l = open("link.txt", "r")
        litterbox = l.readlines()
        link = litterbox[0]
        l.close()
        change = True        
        
    f.close()

    # update status if new song as of rn
    if change == True:
        RPC.update(
                details = song,
                state = "by" + artist,
                #state = curr_min + ":" + curr_sec + "/" + end_min + ":" + end_sec, 
                large_image = link,
                large_text = album + "-" + year,
                start = start_time,
                #end = end_time,
                instance = True
                )

    time.sleep(TIME) 

RPC.close()
