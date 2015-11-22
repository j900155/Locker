import urllib2
import requests
import time
import serial


user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
first=True
step=0
html=''
t1=''
t2=''
#-----------------check reader
while True:
	try:  
		ser = serial.Serial('/dev/ttyACM0',115200)
	except Exception:
		print "not Connection"
		break

	
	if first:	
		
		print  ser.readline()
		first=not first
	
	s=ser.readline()
#----------start
	if step==0:
		print s
		print s[0:4]
		step=1
	if s.find("user")!=-1 and step==1:
		 		
		t1=s[5:]
		print 'user'+'  '+str(t1) 
		step=2
		s=ser.readline()
		print s
		
		url='http://127.0.0.1:8000/index/?pw='+str(t1)
		

		print url

		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		html = response.read()
		#print html
#----who are you
	if html.find('<title>box</title>')==-1:
			print 'open'
			
			url='http://127.0.0.1:8000/user/?NFC_PW='+str(t1)
			print url
			req = urllib2.Request(url)
			response = urllib2.urlopen(req)
			html = response.read()
	#	print html
			if html.find('<title>index</title>')!=-1:
				print 'fail  return to index'
				step=0	
			else:	
				io=html.find('<p name=\'io\'>')
				print html[io+13:io+15]
				print 'wahaha!'
				step=0
				print step	
			ser.write('finish')

	else:	
			if  step==2:
				print 'box'
				start=html.find('<p name=\"t\">')
				start=start+12
				end=html.find('</p>',start)
				all_box=html[start:end]
				print all_box
				print 'write'
				ser.write(all_box)
#			   	0123456789012345678901234
#				0000000000000000000000000
#				
				
				print 'end'
				time.sleep(1)
#				
				s=ser.readline()
				step=3
				print s[0:6]
				print step
				print '5555'
			if  step==3 :
				while s.find('request')==-1:
				 	s=ser.readline()
					print 'while'
				
				print str(s)+'  out'			
				p1=s.find(':')
				p2=s.find(';')
				print str(p1)+' '+str(p2) 		
				t2=s[p2+1:-2]
				print t2
				t1=s[p1+1:p2]
				print t1
				url='http://127.0.0.1:8000/box/?id='+str(t2)+'&pw='+str(t1)
				req = urllib2.Request(url)
				response = urllib2.urlopen(req)
				print url
				ser.write('OK')
				print 'over'
				
				step=0
	
	
	
	
