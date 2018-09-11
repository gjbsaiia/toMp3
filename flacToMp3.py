#!/usr/bin/python

# Griffin Saiia, ffmpeg wrapper to convert .flac to .mp3

import os
import sys
import subprocess

class fileData:
	def __init__(self):
		self.name = ""
		self.path = ""
		self.ext = ""

def main():
	print("Welcome to Griffin's audio file converter!")
	print("Special thanks to the genius' who developed ffmpeg")
	print("*****************************************************")
	line = raw_input("single or batch? ")
	print("*****************************************************")
	if(line == "single"):
		line = raw_input("Enter the path to your .flac file: ")
		print("*****************************************************")
		fileD = fileData()
		extractData(fileD, line)
		input = fileD.path+fileD.name+"."+fileD.ext
		output = fileD.path+fileD.name+".mp3"
		command = "ffmpeg -i "+input+" -ab 320k -map_metadata 0 -id3v2_version 3 "+output
		print("converting "+fileD.name+"."+fileD.ext+"...")
		subprocess.check_output(command, shell=True)
		print("...done")
		print("*****************************************************")
	else:
		line = raw_input("Enter the path to your directory: ")
		print("*****************************************************")
		fileArray = []
		fileArray = scanDir(line, fileArray)
		moreThanOne(fileArray)
	print("happy listens")

def scanDir(directory, fileArray):
	print("scanning directory...")
	for file in os.listdir(directory):
		split = file.split(".")
		if(split[1] == "flac"):
			fileD = fileData()
			fileD.path = directory
			fileD.name = split[0]
			fileD.ext = split[1]
			fileArray.append(fileD)
	print("...files gathered.")
	print("*****************************************************")
	return fileArray

def moreThanOne(fileArray):
	for fileD in fileArray:
		input = fileD.path+fileD.name+"."+fileD.ext
		output = fileD.path+fileD.name+".mp3"
		command = "ffmpeg -i "+input+" -ab 320k -map_metadata 0 -id3v2_version 3 "+output
		print("converting "+fileD.name+"."+fileD.ext+"...")
		subprocess.check_output(command, shell=True)
		print("...done")
	print("*****************************************************")

def extractData(fileD, raw):
	firstsplit = raw.split("/")
	i = 0
	while(i < (len(firstsplit) - 1)):
		if(firstsplit[i] != ''):
			fileD.path = fileD.path + "/" + firstsplit[i]
		i += 1
	if(fileD.path != ''):
		fileD.path = fileD.path + "/"
	secondsplit = firstsplit[(len(firstsplit)-1)].split(".")
	fileD.name = secondsplit[0]
	fileD.ext = secondsplit[1]


# to run it from command line
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("")
		print('Interrupted')
        try:
			sys.exit(0)
	except SystemExit:
			os._exit(0)
