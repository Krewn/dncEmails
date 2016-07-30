#print "Importing Mechanize"
import mechanize
#print "Importing BeautifulSoup"
import BeautifulSoup

#print "Initializing Mechanize Browser"
chrome = mechanize.Browser()
chrome.set_handle_robots(False)
chrome.addheaders = [('User-agent', '')]

#print "Defining Methods"
def snag(n):
	global chrome
	htmltext = chrome.open("https://wikileaks.org/dnc-emails/emailid/"+str(n)).read()
	soup = BeautifulSoup.BeautifulSoup(htmltext)
	content = soup.find("div", {"id": "content"})
	subject = content.find("h2").getText()
	meta = content.find("header").getText()
	meta = meta.split("\n")
	sender = meta[0].split("From:")[1]
	recieverAndDate = meta[1].split("To:")[1].split("Date")
	reciever = recieverAndDate[0]
	date = recieverAndDate[1]
	text = content.find("div",{"id":"uniquer"}).getText()
	op = {'from':sender,'to':reciever,'subject':subject,'contnet':text,'date':date}
	return(op)

#print "Scraping::"
more = True
n = 1
"""
while(more):
	try:
		print str(n)
		emailDict = snag(n)
		outPut = open(str(n),"w")
		outPut.write(str(emailDict))
		outPut.close()
		n+=1
	except AttributeError:
		print f
		more = False
"""
def snagRange(start,end):
	for k in range(start,end):
		emailDict = snag(k)
		outPut = open(str(k),"w")
		outPut.write(str(emailDict))
		outPut.close()
