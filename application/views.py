from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.http import JsonResponse

user=""
password =""
userID = 0
desig = ""
# Create your views here.
def home(request):
    if request.method == "GET":
        print("GET")
        return render(request,"index.html",{"credMsg":""})
    elif request.method == "POST":
        data = {
        "stageCom" : "s4",
        "urlCome" : "",
        "firstname":user.first_name,
        "lastname":user.last_name,
        "status": "pending",
        "color" : "yellow",
        "message" : "Your Application is pending for approval",
        }
        print("POST")
        try:
            caste_certi = request.POST.get("caste_certi")
            income_certi = request.POST.get("income_certi")
            Aadhaar_card = request.POST.get("Aadhaar_card")
            photo = request.POST.get("photo")
            sign = request.POST.get("sign")
            fee_receipt = request.POST.get("fee_receipt")
            
            new_entry = AppDocInfo(username=user,casteCerti=caste_certi,incomeCerti=income_certi,aadhaar=Aadhaar_card,photo=photo,sign=sign,
            addmissionLetter=fee_receipt)
            new_entry.save()
            return render(request,"profile.html",data)
        except Exception as e:
            return HttpResponse("error : "+e)


def profile(request):
    global userID,user,desig
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        desig = request.POST.get("desig")
        print(desig)
        print(username)
        # print(password)
        user = authenticate(username=str(username), password=str(password))
        # print(user.groups.filter(name=desig).exists())
        if user is not None:
            if (user.groups.filter(name=desig).exists()):
                login(request,user)
                user = User.objects.get(username=username)
                userID = user.id
            else:
                return render(request,"index.html",{"credMsg":"Wrong Designation"})
        else:
            return render(request,"index.html",{"credMsg":"Invalid Credentials"})
    if (desig == "student" ):
        user1=AppPerInfo.objects.filter(username=userID)
        user2=AppEduInfo.objects.filter(username=userID)
        user3=AppBanInfo.objects.filter(username=userID)
        user4=AppDocInfo.objects.filter(username=userID)
        rejectHod = HodReject.objects.filter(username = userID)
        rejectpri = PrincipalReject.objects.filter(username = userID)
        approved = PrincipalApprove.objects.filter(username=userID)
        data = {
            "stageCom" : "",
            "urlCome" : "appPerInfo",
            "firstname":user.first_name,
            "lastname":user.last_name,
            "status": "pending",
            "color" : "yellow",
            "message" : "Your Application is pending for approval",
        }
        if user1.exists() :
            if user2.exists():
                if user3.exists():
                    if user4.exists():
                        # print(50)
                        data["stageCom"]="s4"
                        data["urlCome"]=""
                        if approved.exists():
                            data["status"] = "Approved"
                            data["color"]="green"
                            data["message"] = "Your Scholarship Application Has Been APPROVED."
                        elif (rejectHod.exists()):
                            
                            data["status"] = "Rejected"
                            data["color"]="Red"
                            data["message"] = f"Your Scholarship Application Has Been REJECTED."
                        elif (rejectpri.exists()):
                            data["status"] = "Rejected"
                            data["color"]="Red"
                            data["message"] = f"Your Scholarship Application Has Been REJECTED."
                        pass    
                    else:
                        data["stageCom"]="s3"
                        data["urlCome"]="appDocInfo"
                        pass
                else:
                    data["stageCom"]="s2"
                    data["urlCome"]="appBanInfo"
                    pass
            else:
                data["stageCom"]="s1"
                data["urlCome"]="appEduInfo"
                pass
        else:
            pass
        # print(data)
        return render(request,"profile.html",data)
    elif (desig == "hod"):
        return render(request, "hodPofile.html")
    elif(desig == "principal"):
        return render(request, "principalProfile.html")

def logoutfunc(request):
    logout(request)
    return render(request,"index.html",{"credMsg":""})
def appPerInfo(request):
    return render(request,"application_per_info.html")
def appEduInfo(request):
    if request.method == "POST":
        try:
            full_name = request.POST.get("full_name")
            dob = request.POST.get("dob")
            gender = request.POST.get("gender")
            category = request.POST.get("category")
            cat_certi_no = request.POST.get("cat_certi_no")
            aadhaar_number = request.POST.get("aadhaar_number")
            father_name = request.POST.get("father_name")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            annual_income = request.POST.get("annual_income")
            address = request.POST.get("address")
            pincode = request.POST.get("pincode")
            
            newEntry= AppPerInfo(username = user ,fullName=full_name,dob=dob,gender=gender,category=category,caste_certi_no=cat_certi_no,aadhar=aadhaar_number,father=father_name,phone=phone,email=email,income=annual_income,address=address,pincode=pincode)
            newEntry.save()
        except Exception as e:
            return HttpResponse(e)
    return render(request,"application_edu.html")
def appBanInfo(request):
    if request.method == "POST":
        try:
            edu_level = request.POST.get("edu_level")
            edu_level = request.POST.get("institute_name")
            inst_address = request.POST.get("inst_address")
            enrollment = request.POST.get("enrollment")
            course = request.POST.get("course")
            study_year = request.POST.get("study_year")
            percentage = request.POST.get("percentage")
            passing_year = request.POST.get("passing_year")
            marksheet = request.POST.get("marksheet")

            new_entry = AppEduInfo(username=user,eduLevel=edu_level,InstName=edu_level,address=inst_address,enrollment=enrollment,program=course,year=study_year,percent=percentage,passingYear=passing_year,marksheet=marksheet)
            new_entry.save()
        except Exception as e :
            return HttpResponse("error : "+e)
    return render(request,"application_bank.html")
def appDocInfo(request):
    if request.method == "POST":
        try:
            acc_name = request.POST.get("acc_name")
            acc_num = request.POST.get("acc_num")
            bank_name = request.POST.get("bank_name")
            branch_name = request.POST.get("branch_name")
            ifsc = request.POST.get("ifsc")
            
            new_entry=AppBanInfo(username=user,accHolderName=acc_name,accNumber=acc_num,bankName=bank_name,branchName=branch_name,ifsc=ifsc)
            new_entry.save()
        except Exception as e :
            return HttpResponse("error : "+e)
            pass
    return render(request,"application_doc.html")

def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def newUser(request):
    if request.method == "GET":
        return render(request,"newUser.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        desig = request.POST.get("desig")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        print(desig)
        newuser = User.objects.create_user(username=username, email=email, password=password,first_name=firstName,last_name=lastName)
        group = Group.objects.get(name=desig) 
        newuser.groups.add(group)
        return render(request,"index.html")
