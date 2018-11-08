#
import os

phn2IPA = {}
rfile = open('./phone2IPA.conf', 'r')
for line in rfile.readlines():
	phn, num, IPA = line.split()
	phn2IPA.update({phn:IPA})

rfile.close()
wfile = open('./contents.txt', 'w')
filedirs = os.listdir('./')
for file in filedirs:
	if '_' in file and os.path.isdir(file):
		phn1, phn2 = file.split('_')
		IPA1 = phn2IPA.get(phn1)
		IPA2 = phn2IPA.get(phn2)
		wfile.write(phn1+'_'+phn2+' ==> ('+IPA1+'_'+IPA2+')\n')

wfile.close()
