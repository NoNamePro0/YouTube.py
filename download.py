import os
import time

filename = "url.txt"

while True:
    with open(filename ) as f:
        lines = f.readlines()

    if not lines:
        print('The file ' + filename + ' is empty')
        quit()

    url = lines[0]

    os.system('youtube-dl ' + url)
    os.system('clear')

    with open(filename, 'r+') as f:
        t = f.read()
        to_delete = lines[0].strip()
        f.seek(0)
        for line in t.split('\n'):
            if line != to_delete:
                f.write(line + '\n')
        f.truncate()

# Copyright 2020 StackNeverFlow
