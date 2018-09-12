#!/usr/bin/python

# Griffin Saiia, ffmpeg wrapper to convert all common audio types to .mp3

import os
import sys
import subprocess

# struct to store file data neatly
class fileData:
	def __init__(self):
		self.name = ""
		self.path = ""
		self.ext = ""

# dictionary to store ffmpeg commands
def flac():
	command = []
	command.append("ffmpeg -i ")
	command.append(" -ab 320k -map_metadata 0 -id3v2_version 3 ")
	command.append(".mp3 >/dev/null 2>&1")
	return command

def m4a():
	command = []
	command.append("ffmpeg -i ")
	command.append(" -acodec libmp3lame -ab 128k -map_metadata 0 ")
	command.append(".mp3 >/dev/null 2>&1")
	return command

def wav():
	command = []
	command.append("ffmpeg -i ")
	command.append(" -vn -ar 44100 -ac 2 -ab 192k -map_metadata 0 -f mp3 ")
	command.append(".mp3 >/dev/null 2>&1")
	return command

def wma():
	command = []
	command.append("ffmpeg -i ")
	command.append(" -acodec libmp3lame -ab 192k -map_metadata 0 ")
	command.append(".mp3 >/dev/null 2>&1")
	return command

def alac():
	command = []
	command.append("ffmpeg -i ")
	command.append(" -ac 2 -f wav -map_metadata 0 - | lame -V 2 -")
	command.append(".mp3 >/dev/null 2>&1")
	return command

def aiff():
	command = []
	command.append("ffmpeg -i ")
	command.append(" -f mp3 -acodec libmp3lame -ab 192000 -ar 44100 -map_metadata 0 ")
	command.append(".mp3 >/dev/null 2>&1")
	return command

commands = {"flac": flac,
			"m4a": m4a,
			"wav": wav,
			"wma": wma,
			"caf": alac,
			"aif": aiff
}

def main():
	print("********************************************************************")
	print("Welcome to Griffin's audio file converter!")
	print("********************************************************************")
	print("Special thanks to the genius' who developed ffmpeg")
	print("**Note: ffmpeg doesn't support the following chars in file names:")
	print("             spaces      '()'      ")
	print("********************************************************************")
	line = raw_input("single or batch? ")
	print("********************************************************************")
	fileArray = []
	if(line == "single"):
		line = raw_input("Enter the path to your .flac file relative to the program: ")
		print("********************************************************************")
		fileD = fileData()
		extractData(fileD, line)
		fileArray.append(fileD)
		convert(fileArray)
	else:
		line = raw_input("Enter the path to your directory relative to the program: ")
		print("********************************************************************")
		fileArray = scanDir(line, fileArray)
		convert(fileArray)
	print("happy listens")

def scanDir(directory, fileArray):
	print("scanning directory...")
	for file in os.listdir(directory):
		split = file.split(".")
		if(split[1] == "flac" or split[1] == "m4a"):
			fileD = fileData()
			fileD.path = directory
			fileD.name = split[0]
			fileD.ext = split[1]
			fileArray.append(fileD)
	print("    ...files gathered.")
	print("********************************************************************")
	return fileArray

def convert(fileArray):
	for fileD in fileArray:
		input = fileD.path+fileD.name+"."+fileD.ext
		output = fileD.path+fileD.name
		commandFrame = commands[fileD.ext]()
		command = commandFrame[0]+input+commandFrame[1]+output+commandFrame[2]
		print("converting "+fileD.name+"."+fileD.ext+"...")
		subprocess.check_output(command, shell=True)
		print("                                                ...done")
	print("********************************************************************")

def extractData(fileD, raw):
	firstsplit = raw.split("/")
	i = 0
	while(i < (len(firstsplit) - 1)):
		if(i == 0):
			fileD.path = firstsplit[i] + "/"
		else:
			fileD.path = fileD.path + firstsplit[i] + "/"
		i += 1
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
