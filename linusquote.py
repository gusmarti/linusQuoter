#!/usr/bin/python3

import random

lines = open("quotes").readlines()
line  = random.mychoice(lines)[:-1:]
print (line)

