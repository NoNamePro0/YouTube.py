import os
import time

filename = "url.txt"

try:
    with open(filename ) as f:
        lines = f.readlines()
        if not lines:
            File = False
        else:
            File = True
except IOError:
    File = False    

if File == False:
    url = input('Please enter YT URL to Download: ')

Download = True
while Download == True:
    if File == True:
        with open(filename ) as f:
            lines = f.readlines()
            if lines:
                url = lines[0]
            
    if url and not url.__eq__('\n'):
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
    else:
        Download = False

# Copyright 2020 StackNeverFlow
