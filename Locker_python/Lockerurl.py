import urllib2
import requests

t1='IMAC'
t2='123'

url='http://127.0.0.1:8000/index/?pw='+str(t1)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

print url

req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()
#print html
if html.find('<title>open</title>')!=-1:
	print 'open'
	t1='test'
	url='http://127.0.0.1:8000/user/?NFC_PW='+str(t1)
	print url
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	html = response.read()
#	print html
	if html.find('<title>index</title>')!=-1:
		print 'fail  return to index'	
	else:	
		io=html.find('<p name=\'io\'>')
		print html[io+13:io+15]
else:
	print 'box'
	start=html.find('<p name=\"t\">')
	start=start+12
	end=html.find('</p>',start)
	print html[start:end]
	t1=raw_input('id')
	t2=raw_input('pw')
	url='http://127.0.0.1:8000/box/?id='+str(t1)+'&pw='+str(t2)
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	print url
	
	
	
	
