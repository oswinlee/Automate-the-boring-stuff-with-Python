#！python3
#this program is to search a regex entered by user from all txt files that from the CWD, 
#and print all matched lines from txt file
import os,re
allFileName = os.listdir('d:\\python')
txtFileName = []
#creates Regex for searching txt file
txtRegex = re.compile(r'.txt$')
#find out all txt file and add them into txtFileName
for i in range(len(allFileName)):
	if txtRegex.search(allFileName[i]) != None:
		txtFileName.append(allFileName[i])
print(txtFileName)
print('Please enter a Regex for matching:')
userRegex = re.compile(str(input()))
for i in range(len(txtFileName)):
	txtFile = open('d:\\python\\' + txtFileName[i],encoding = 'UTF-8')
	txtFileLines = txtFile.readlines()
	txtFile.close()
	for j in range(len(txtFileLines)):
		if userRegex.search(txtFileLines[j]) != None:
			print('Find one matched lines in %s file line %d' %(txtFileName[i],j+1))
			print('The matched lines as below:')
			print(txtFileLines[j])
