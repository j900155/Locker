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
	
	
#----------start
	if step==0:
		s="user"	
		print s
		ser.write("read")
		check="1234"
		while check[:-2]!="read":
			print str(check)+"  r1 "
			check=ser.readline()
		print check	
		step=1
	if  step==1: 		
		t1=ser.readline()
		t2=t1[:4]
		print 'user'+'  '+str(t2) 
		

		url='http://127.0.0.1:8000/index/?pw='+str(t2)
		print url

		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		html = response.read()
#		print html
		
		step=2
		print "step 2"
#----who are you
	if html.find('<title>box</title>')==-1:
			print 'open'
			p1=t1.find(';')
			t1=t1[:p1]	
			url='http://127.0.0.1:8000/user/?NFC_PW='+str(t1)
			print url
			req = urllib2.Request(url)
			response = urllib2.urlopen(req)
			html = response.read()
	#	print html
			if html.find('<title>index</title>')!=-1:
				print 'fail  return to index'
				step=0
				time.sleep(3)	
			else:	
				io=html.find('<p name=\'io\'>')
				print html[io+13:io+15]
				print 'wahaha!'
				step=0
				print step	
				time.sleep(3)

	else:	
			if  step==2:
				print 'box'
				start=html.find('<p name=\"t\">')
				start=start+12
				end=html.find('</p>',start)
				all_box=html[start:end]
				print all_box
				print 'write'
				ser.write("write")
				check="1234"
				while check[:-2]!="write":
					check=ser.readline()
					print "step  2"
				check=""
				ser.write(all_box)
#			   	0123456789012345678901234
#				0000000000000000000000000
#				
#				
				time.sleep(0.5)
				print ser.readline()
				step=3
				print 'step '+str(step)
			if  step==3 :			
				ser.write('read')
				check="1234"
				while check[:-2]!="read":
					check=ser.readline()
				s=""
				s=ser.readline()	
				
				p1=s.find(';')
				print str(p1) 		
				t2=s[p1+1:-5]
				print t2
				t1=s[:p1]
				print t1
				url='http://127.0.0.1:8000/box/?id='+str(t2)+'&pw='+str(t1)
				req = urllib2.Request(url)
				response = urllib2.urlopen(req)
				print url
				print 'over'
				time.sleep(3)	
				step=0
	
	
	
	
