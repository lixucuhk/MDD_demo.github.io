phn2IPA = {}
rfile = open('./phone2IPA.conf', 'r')
for line in rfile.readlines():
	phn, num, IPA = line.split()
	phn2IPA.update({phn:IPA})

rfile.close()

rfile = open('./index.html', 'r')
wfile = open('./index1.html', 'w')

T = 0
context = []

for line in rfile.readlines():
	if '<b>' in line and '<td' in line:
		part1, part2 = line.split('\"center\"')
		text = part1+'\"center\"'+' rowspan=\"2\"'+part2
		wfile.write(text)
		T = 1
	else:
		wfile.write(line)
		if '<source src' in line:
			text = line.split('/')[-2].split('_')[3:]
			text[-1] = text[-1].split('.')[0]
			context.append(text) 
		if '</tr>' in line and T == 1:
			wfile.write('      <tr>\n')
			for i in range(len(context)):
				wfile.write('        <td align=\"center\" >')
				text = context[i]
				IPAtext = []
				for j in range(len(text)):
					if '0' in text[j]:
						if text[j][-1] == '0':
							text[j] = text[j][:-1]
							if phn2IPA.get(text[j])==None:
								print(text)
							IPAtext.append(phn2IPA.get(text[j]))
						else:
							text[j] = text[j].replace('0', '_')
							phn1, phn2 = text[j].split('_')
							IPAtext.append(phn2IPA.get(phn1)+'_'+phn2IPA.get(phn2))
					else:
						if phn2IPA.get(text[j])==None:
							print(text)
						IPAtext.append(phn2IPA.get(text[j]))
					wfile.write(text[j]+' ')
				wfile.write('(')
				for j in range(len(IPAtext)-1):
					wfile.write(IPAtext[j]+' ')
				wfile.write(IPAtext[-1]+')</td>\n')
			wfile.write('      </tr>\n')
			context = []
			T = 0
rfile.close()
wfile.close()
