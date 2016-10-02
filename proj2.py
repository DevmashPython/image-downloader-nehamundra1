import urllib
import re
f= open("proj21.txt","w")
z="https://www.tutorialspoint.com/"
url= urllib.urlopen(z)
html=url.read()
b= re.compile("<img.*src=\"([^ ]*)\"")
x= re.findall(b,html)
for i in x:
	if i.startswith("/"):
		print "https://www.tutorialspoint.com" +i
		f.write ("https://www.tutorialspoint.com"+i +"\n")
	else:
		print z+i
		f.write (z+i+"\n")
f.close()
