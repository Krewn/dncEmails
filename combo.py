import os

text= ""
subject= ""
for k in range(1,22457):
	try:
		handle = open(str(k),"r")
		content = eval(handle.read())
		text+=" "+content['contnet']
		subject+=" "+content['subject']
		handle.close()
	except IOError:
		print str(k)+" is not a file!"
	if(k%250 == 0):
		print str(k)+"/22457"

opFile = open("aggContent.txt","w")
opFile.write(text.encode("utf-8"))
opFile.close()

opFile = open("aggSubject.txt","w")
opFile.write(subject.encode("utf-8"))
opFile.close()
	
