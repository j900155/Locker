#try get session
import urllib2
import requests
t1=''

t2=''

url='http://127.0.0.1:8000/index/?&pw='+str(t1)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
print url

req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()
check= html.find('True')
if check>-1:
	print True
else:
	print False
print check

