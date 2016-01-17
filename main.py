__author__ = 'shrenilpatel'

import re
import random

start = []
vocals = []
end = []
fend = []

find = re.compile(r"([A-Za-z]+)")
leek = re.compile(r"((?:[^AEIOUaeiouyY\s]+)|(?:[AEIOUaeiouyY]+))([AEIOUaeiouyY]+){0,1}([A-Za-z]+?)((?:(?:[AEIOUYaeiouy])(?:[A-Za-z]+)(?:[AEIOUYaeiouy]))|(?:(?:[AEIOUYaeiouy])(?:[A-Za-z]+))|(?:[AEIOUYaeiouy]))\b")

file = open('fname2', 'r')
full = file.read()

fullArr = filter(None, full.split('\n'))

print fullArr

for l in fullArr:
    name = re.search(find, l).group(1)
    tube = re.search(leek, l)
    try:
        start.append(tube.group(1).lower())
    except:
        pass
    try:
        vocals.append(tube.group(2).lower())
    except:
        pass
    try:
        end.append(tube.group(3).lower())
    except:
        pass
    fend.append(tube.group(4).lower())

#uncomment for Specific name starters
#start = ["kr", "kh", "khy", "ksh", "k", "gh", "g", "qu", "c", "ch",]

for i in range(0,30):
    if random.choice([0,0]) == 0:
        print random.choice(start) + random.choice(vocals) + random.choice(end) + random.choice(fend)
    else:
        print random.choice(start) +  random.choice(fend)