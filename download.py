import os
import time

filename = "url.txt"

with open(filename ) as f:
    lines = f.readlines()
    if not lines:
        File = False
        url = input('Please enter YT URL to Download: ')
    else:
        File = True

Download = True

while Download == True:
    if File == True:
        with open(filename ) as f:
            lines = f.readlines()
            if lines:
                url = lines[0]
            
    os.system('youtube-dl ' + url)

    if File == True:
        with open(filename, 'r+') as f:
            t = f.read()
            to_delete = lines[0].strip()
            f.seek(0)
            for line in t.split('\n'):
                if line != to_delete:
                    f.write(line + '\n')
            f.truncate()
    else:
        Download = False

# Copyright 2020 StackNeverFlow
