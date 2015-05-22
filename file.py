import re
infile = open('negro.html') 
#infile = open('bro.html')
outfile = open('n.html', 'w')
#for line in infile:
for line in infile:
	#	line = line.replace(src, target)
	line = re.sub('\[.*\]','',line,re.IGNORECASE)
	line = re.sub('</h.*>','<p>',line,re.IGNORECASE)
	
	outfile.write(line)
infile.close()
outfile.close()