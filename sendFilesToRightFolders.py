import sys
import os
from os import listdir
from os.path import isfile, join
import shutil


def main(folderWithFiles, destUberFolder):
	#onlyfiles = [ f for f in listdir(folderWithFiles) if isfile(join(folderWithFiles,f)) ]
	for dirName, subDirList, fileList in os.walk(folderWithFiles):
		for fname in fileList:
			try:
				currentExtension = fname.split('.')[-1]
				currentPath = os.path.join(dirName, fname)
				desinationPath = os.path.join(destUberFolder,currentExtension,fname)
				shutil.move(currentPath, desinationPath)
			except Exception as e:
				print str(e)
				continue


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Usage: python <PY file name> <full folder path> <destination uber folder>"
		exit(1)

	main(sys.argv[1], sys.argv[2])