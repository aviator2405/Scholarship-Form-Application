from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from application.models import *
from application.serializer import *
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

@api_view(["POST","GET"])
def formFilled(request):
    obj = AppDocInfo.objects.all()
    print(obj)
    serializers = AppDocInfoSerializer(obj, many=True)
    return Response(serializers.data)

@api_view(["GET"])
def userDetails(request,userID):
    obj = User.objects.filter(id=userID)
    serializers= UserSerializer(obj,many=True) 
    return Response(serializers.data)   
    
@api_view(["POST"])
def hodapproved(request):
    if request.method == 'POST':
        serializer = HodApproveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def hodrejected(request):
    if request.method == 'POST':
        serializer = HodRejectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            get = request.data
            print (get["username"])
            print(get["rejectMessage"])
            user = User.objects.get(id = get["username"])
            fullname = str(user.first_name)+" "+str(user.last_name)
            email = str(user.email)
            print(fullname)
            subject = "Unfortunately, Your Application has been Rejected"
            from_email = "aviatordev240502@gmail.com"
            # test_email="priyasaini1373@gmail.com"
            to = [email, "aviatordev240502@gmail.com"]
            html_content = f"<h1>Unfortunately, Your Application has been rejected</h1><br><p style='font-size: large;'>Dear {fullname},<br><br>I hope this message finds you well. We appreciate your interest in the <b>JEC Scholarship</b> and the time and effort you put into your application. After reviewing your submission, we regret to inform you that we are <b>unable to proceed with your application</b> at this time.<br><br>The selection committee noted that <b>{get['rejectMessage']}</b>. Unfortunately, this has affected the evaluation process, and <b>we cannot move forward</b> with your application.<br><br>We encourage you to carefully review the application guidelines and consider reapplying in the future if another opportunity arises. Should you have any questions or require clarification on the submission process, please feel free to reach out to us.<br><br>Thank you once again for your interest in the JEC Scholarship. We wish you success in your academic pursuits.<br><br><b>Best regards,</b><br><br>Dr. Rahul Walia<br>Head of JEC Scholarship Department<br>JEC Engineering College, Jabalpur<br>+91-9039972014<br>rp240502@gmail.com"
            msg = EmailMultiAlternatives(subject, html_content, from_email, to)
            msg.content_subtype='html'
            msg.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def principalapproved(request):
    if request.method == 'POST':
        serializer = PrincipalApproveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            get = request.data
            print (get["username"])
            user = User.objects.get(id = get["username"])
            fullname = str(user.first_name)+" "+str(user.last_name)
            email = str(user.email)
            print(fullname)
            subject = "Congratulations! Your Scholarship Application Has Been Accepted."
            from_email = "aviatordev240502@gmail.com"
            # test_email="priyasaini1373@gmail.com"
            to = [email, "aviatordev240502@gmail.com"]
            html_content = f"<h1>Congratulations! Your Scholarship Application Has Been Accepted</h1><br><p style='font-size: large;'>Dear {fullname},<br><br>I hope this email finds you well. We are pleased to inform you that after careful consideration, your application for the <b>JEC Scholarship</b> has been <b>accepted</b>. Your outstanding academic achievements and dedication have impressed the selection committee, and we are excited to offer you this scholarship.<br><br>This scholarship award includes <b>full fee payment for education</b>. We believe that this scholarship will significantly contribute to your educational journey and help you achieve your academic and career goals.<br><br>Congratulations once again on this well-deserved achievement. We look forward to supporting you in your future endeavors.</p><br><br><b>Best regards,</b> <br><br>Dr. Rahul Walia<br>Head of JEC Scholarship Department <br>Jabalpur Engineering College, Jabalpur <br>+91-9039972014<br>rp240502@gmail.com<br>"
            msg = EmailMultiAlternatives(subject, html_content, from_email, to)
            msg.content_subtype='html'
            msg.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def principalrejected(request):
    if request.method == 'POST':
        serializer = PrincipalRejectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            get = request.data
            print (get["username"])
            print(get["rejectMessage"])
            user = User.objects.get(id = get["username"])
            fullname = str(user.first_name)+" "+str(user.last_name)
            email = str(user.email)
            print(fullname)
            subject = "Unfortunately, Your Application has been Rejected"
            from_email = "aviatordev240502@gmail.com"
            # test_email="priyasaini1373@gmail.com"
            to = [email, "aviatordev240502@gmail.com"]
            html_content = f"<h1>Unfortunately, Your Application has been rejected</h1><br><p style='font-size: large;'>Dear {fullname},<br><br>I hope this message finds you well. We appreciate your interest in the <b>JEC Scholarship</b> and the time and effort you put into your application. After reviewing your submission, we regret to inform you that we are <b>unable to proceed with your application</b> at this time.<br><br>The selection committee noted that <b>{get['rejectMessage']}</b>. Unfortunately, this has affected the evaluation process, and <b>we cannot move forward</b> with your application.<br><br>We encourage you to carefully review the application guidelines and consider reapplying in the future if another opportunity arises. Should you have any questions or require clarification on the submission process, please feel free to reach out to us.<br><br>Thank you once again for your interest in the JEC Scholarship. We wish you success in your academic pursuits.<br><br><b>Best regards,</b><br><br>Dr. Rahul Walia<br>Head of JEC Scholarship Department<br>JEC Engineering College, Jabalpur<br>+91-9039972014<br>rp240502@gmail.com"
            msg = EmailMultiAlternatives(subject, html_content, from_email, to)
            msg.content_subtype='html'
            msg.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def ApprovedByHOD(request):
    obj = HodApprove.objects.all()
    serializers= HodApproveSerializer(obj,many=True) 
    return Response(serializers.data)  

@api_view(['DELETE'])
def delete_user_form_HOD(request, userID):
    print (userID)
    try:
        form1 = AppPerInfo.objects.get(username=userID)
        form2 = AppEduInfo.objects.get(username=userID)
        form3 = AppBanInfo.objects.get(username=userID)
        form4 = AppDocInfo.objects.get(username=userID)
    except AppPerInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        form1.delete()
        form2.delete()
        form3.delete()
        form4.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_user_form_PRI(request, userID):
    try:
        form1 = AppPerInfo.objects.get(username=userID)
        form2 = AppEduInfo.objects.get(username=userID)
        form3 = AppBanInfo.objects.get(username=userID)
        form4 = AppDocInfo.objects.get(username=userID)
        hodApporved=HodApprove.objects.get(username = userID)
    except AppPerInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        form1.delete()
        form2.delete()
        form3.delete()
        form4.delete()
        hodApporved.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
finalData={}
@api_view(["GET"])
def getPerInfo(request,userID):
    obj = AppPerInfo.objects.filter(username=userID)
    serializers= AppPerInfoSerializer(obj,many=True) 
    finalData = serializers.data   
    obj = AppEduInfo.objects.filter(username=userID)
    serializers= AppEduInfoSerializer(obj,many=True) 
    finalData += serializers.data
    obj = AppBanInfo.objects.filter(username=userID)
    serializers= AppBanInfoSerializer(obj,many=True) 
    finalData += serializers.data
    obj = AppDocInfo.objects.filter(username=userID)
    serializers= AppDocInfoSerializer2(obj,many=True) 
    finalData += serializers.data
    return Response(finalData)

@api_view(["GET"])
def ApprovedByPRI(request):
    obj = PrincipalApprove.objects.all()
    serializers= PrincipalApproveSerializer(obj,many=True) 
    return Response(serializers.data)  
