nothing = 90052
import os
from zipfile import ZipFile
comments=""
file_names = os.listdir('/Users/saahumad/Documents/MyPythonScripts/pythonchallenge.com/c6_files/channel/')
while True:
	with open(f'/Users/saahumad/Documents/MyPythonScripts/pythonchallenge.com/c6_files/channel/{nothing}.txt') as file:
		file_content = file.read()
	try:
		nothing = int(file_content.split()[-1])
		with ZipFile('/Users/saahumad/Documents/MyPythonScripts/pythonchallenge.com/c6_files/channel.zip','r') as zip:
			comments+=(zip.getinfo(f'{nothing}.txt').comment.decode('UTF-8'))
	except:
		print(comments)
		print(file_content)
		break

#Result:
#(base) saahumad@SAAHUMAD-M-82HG pythonchallenge.com % python c6.py
#***************************************************************
#****************************************************************
#**                                                            **
#**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
#**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
#**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
#**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
#**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
#**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
#**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
#**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
#**                                                            **
#****************************************************************
# **************************************************************
#
#Collect the comments.

#then Get html for http://www.pythonchallenge.com/pc/def/hockey.html:
#it's in the air. look at the letters.
#oxygen


#for x in file_names:
#	with ZipFile('/Users/saahumad/Documents/MyPythonScripts/pythonchallenge.com/c6_files/channel.zip','r') as zip:
#		print(zip.getinfo(str(x).replace("'","")).comment)
#	with open(f'/Users/saahumad/Documents/MyPythonScripts/pythonchallenge.com/c6_files/channel/{x}') as file2:
#		file2_content = file2.read()
#	if "Next nothing is" not in file2_content:
#		print(file2_content)
