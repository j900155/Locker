from django.contrib import admin

# Register your models here.

from GetNFC.models import NFC,Member,Box
class NFCAdmin(admin.ModelAdmin):
	fields=['NFC_PW','IO']
	list_display=('NFC_PW','IO')
admin.site.register(NFC,NFCAdmin)

class MemberAdmin(admin.ModelAdmin):
	fields=['user']
#	list_display=('user')
admin.site.register(Member,MemberAdmin)

class BoxAdmin(admin.ModelAdmin):
	fields=['Box_id','Box_use','Box_size']
	list_display=('Box_id','Box_use','Box_size')
admin.site.register(Box,BoxAdmin)


	
