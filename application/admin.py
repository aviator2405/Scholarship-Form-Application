from django.contrib import admin
from .models import *
# Register your models here.

class AppEduInfoAdmin(admin.ModelAdmin):
    list_display = ["username","eduLevel","InstName","address","enrollment","program","year","percent","passingYear","marksheet"]

class AppPerInfoAdmin(admin.ModelAdmin):
    list_display = ["username","fullName","dob","gender","category","caste_certi_no","aadhar","father","phone","email","email","address","pincode"]

class AppBanInfoAdmin(admin.ModelAdmin):
    list_display=["username",'accHolderName','accNumber','bankName','branchName','ifsc']

class AppDocInfoAdmin(admin.ModelAdmin):
    list_display=['username','casteCerti','incomeCerti','aadhaar','photo','sign','addmissionLetter']

class FormStatusAdmin(admin.ModelAdmin):
    list_display= ["username","status"]

class HodApproveAdmin(admin.ModelAdmin):
    list_display = ["username"]

class HodRejectAdmin(admin.ModelAdmin):
    list_display=["username","rejectMessage"]

class PrincipalApproveAdmin(admin.ModelAdmin):
    list_display = ["username"]

class PrincipalRejectAdmin(admin.ModelAdmin):
    list_display=["username","rejectMessage"]


admin.site.register(AppPerInfo, AppPerInfoAdmin)
admin.site.register(AppEduInfo, AppEduInfoAdmin)
admin.site.register(AppBanInfo, AppBanInfoAdmin)
admin.site.register(AppDocInfo, AppDocInfoAdmin)
admin.site.register(FormStatus, FormStatusAdmin)
admin.site.register(HodApprove, HodApproveAdmin)
admin.site.register(HodReject, HodRejectAdmin)
admin.site.register(PrincipalApprove, PrincipalApproveAdmin)
admin.site.register(PrincipalReject, PrincipalRejectAdmin)