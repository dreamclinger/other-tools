import glob
from fnmatch import fnmatch
import os

pattern=['.ch.srt', '.chn.srt', '.chn1.srt', '.ch.ass', '.chn.ass', '.chn1.ass']
path='../'

#for filename in os.listdir('.'):
for filename in os.listdir(path):
	for i in range(0,len(pattern)):
		if fnmatch(filename, '*'+pattern[i]):
			if fnmatch(filename, '*.srt'):
				newfilename = filename[0:len(filename)-len(pattern[i])]+'.srt' 
			elif fnmatch(filename, '*.ass'): 
				newfilename = filename[0:len(filename)-len(pattern[i])]+'.ass' 
			os.rename(path+filename, path+newfilename)
			print path+filename + ' -> ' + path+newfilename   

######################################################
## Other Alternative Approach, by using glob module ##
######################################################
# pattern1='.ch.srt'
# 
# for filename1 in glob.glob('*'+pattern1):
# 	newfilename1 = filename1[0:len(filename1)-len(pattern1)]+'.srt' 
# 	print filename1 + ' -> ' + newfilename1   
# 	os.rename(filename1, newfilename1)
