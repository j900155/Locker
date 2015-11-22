from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from GetNFC.models import NFC,Box,Member

import hashlib
#import openio
# Create your views here.

def vindex(request):
	if request.GET:
		r=request.GET['pw']
		check=NFC.objects.get(IO='root')
		
		if  check.NFC_PW==r:
			return HttpResponseRedirect('/box/')
		else:
			return HttpResponseRedirect('/user/')
	return render_to_response('index.html',locals())

def vbox(request):
	Boxs=Box.objects.all()
	NFCs=NFC.objects.all()
	t=""
	for i in Boxs:
		if i.Box_use=="T":
			t=t+"1"
		else:
			t=t+"0"		
	if request.GET:
		Box_id=request.GET['id']
		pw=request.GET['pw']
		m = hashlib.md5()
		m.update(str(pw))
		pw=m.hexdigest()
		if not (NFC.objects.filter(NFC_PW=pw)):
			Box.objects.filter(Box_id=Box_id).update(Box_use='T')
			NFC.objects.create(
				NFC_PW=pw,
				IO=Box_id
			)
			return HttpResponseRedirect('/index/')
		else:
			size="enter pw"
	return render_to_response('web_box.html',locals())

def vuser(request):
	
	NFCs=NFC.objects.all()
	if request.GET:
		inpw=request.GET['NFC_PW']
		check1=NFC.objects.filter(NFC_PW=inpw)
		if len(check1)>0:
			if check1[0].IO=='root':
				io="error"
			elif check1:
				check2=True
				io=check1[0].IO
				Box.objects.filter(Box_id=io).update(Box_use='F')
				NFC.objects.get(NFC_PW=inpw).delete() 				
#				openio.hello()
		else:
			check2=False
			return HttpResponseRedirect('/index/')
	return render_to_response('web_user.html',locals())
