#!/usr/bin/python3

import os
import sys
import time
import extra

os.system('')

endc = "\033[0m"
backLine = "\033[F"

#colors = ["0"]
#colors += [str(i) for i in range(232, 256)]

colors = [str(i) for i in range(17, 22)]
colors += [str(i) for i in [27, 33, 39]]
#colors += [str(i) for i in range(50, 45, -1)]
colors += [str(i) for i in [22, 28, 34, 40, 46]]

def toColor(f):
	n = int(round(((f+1)/2)*len(colors), 0))
	return "\u001b[48;5;" + colors[n] + "m"

octaves = [int(sys.argv[1]), int(sys.argv[2])]

lw, lh = 0, 0

t = time.time()

while True:
	width, height = os.get_terminal_size(1)
	if lw != width or lh != height:
		lw = width
		lh = height
		os.system('cls')
	else:
		print(backLine*height, end="")	

	width, height = width-1, height-1

	lines = ""
	for i in range(height):
		for j in range(width):
			val = extra.perlin_noise(j/octaves[0], i/octaves[1], time.time() - t)
			lines += toColor(val) + " " + endc
		lines += "\n"
	print(lines, end="")
