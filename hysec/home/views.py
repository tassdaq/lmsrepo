from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Profile,lecture,zoom_session,timetables
from django.contrib.auth import get_user_model
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .forms import StudentForm,UpdateStudentForm,UpdateUserForm



# Create your views here.

def index(request):
    return render(request,("index.html"))

def base(request):
    return render (request,("base.html"))



def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def signin(request):
    return render(request,("login.html"))

def courses(request):
    return render(request,("courses.html"))

def profile(request):
    pro = Profile.objects.filter(username = request.user)
    context = {'pro':pro}
    return render(request,'profile.html',context)    

def devop(request):
    return render(request,("devop.html"))

def example(request):
    return render(request,("example.html"))

def student(request): 
    pro = Profile.objects.filter(user = request.user)  
    lec = lecture.objects.filter(username=request.user)
    
    return render(request,'student.html',{'lec': lec,'pro':pro})

def adminportal(request):
   
    return render(request,"adminportal.html")


def studentrecord(request):
    return render(request,("studentrecord.html"))    


def studentlist(request):
    return render(request,("studentlist.html"))



def zoom_meeting(request):
    pro = Profile.objects.filter(user = request.user)  
    z = zoom_session.objects.filter(username = request.user)
    context ={'z':z,'pro':pro} 
    return render(request,'zoom.html',context)   



def time(request):
    pro = Profile.objects.filter(user = request.user)  
    t = timetables.objects.filter(username = request.user)
    context = {'t':t, 'pro':pro}
    return render(request,'timetable.html',context)




def scourse(request):
    pro = Profile.objects.filter(user = request.user)  
    return render(request,'scourse.html',{'pro':pro})

def calender(request):
    return render(request,("calender.html"))


def handlelogout(request):
     logout(request)

     return redirect('home')


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username = username).exists():
        return HttpResponse('<div style="color:red"> This username is already exist </div>')
    else:
           
        return HttpResponse('<div style="color:green">This username is available</div>') 


def handlesignup(request):
    if request.method =="POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        pass1 = request.POST.get('pass1')   

        if password!=pass1:
         messages.error(request,"Password does not match")
         return redirect('home')
        
        if get_user_model().objects.filter(username = username).exists():
         messages.error(request,"Username already exists")
         return redirect('home')   
        #username should be 10 characters

        if len(username) > 10:
         messages.error(request,"Username must be 10 characters") 
         return redirect('home')

         #username should be alphanumeric

        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect('home')
           
        my_user = User.objects.create_user(username,email,password)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.email = email
        my_user.save()
        return redirect('home')

    else:     
        return HttpResponse('404 - Page Not Found')
    

   


def form(request,username):
    
    user = get_object_or_404(User, username=username)
    student_profiles = Profile.objects.filter(user=user)

    if student_profiles.exists():
        # Choose how to handle multiple profiles, for now, taking the first one
        student_profile = student_profiles.first()

        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=user)
            student_profile_form = UpdateStudentForm(request.POST, request.FILES, instance=student_profile)
            if user_form.is_valid() and student_profile_form.is_valid():
                user_form.save()
                student_profile_form.save()
                messages.success(request,"Updated Successfully")
                return redirect('student')  # Redirect to the studentprofile view after updating
                
        else:
            user_form = UpdateUserForm(instance=user)
            student_profile_form = UpdateStudentForm(instance=student_profile)

        context = {
            'user_form': user_form,
            'student_profile_form': student_profile_form,
        }

        return render(request, 'form.html', context)
    else:
        # Handle the case where no profile is found
        return render(request, 'profile_not_found.html')
    

def handlelogin(request): 
    if request.method =="POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('student')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('home')    


    return HttpResponse('handlelogin')     


def studentupdate(request,pk):
    get_update = Profile.objects.get(id=pk)
    return render(request,"updateprofile.html",{'key2':get_update})