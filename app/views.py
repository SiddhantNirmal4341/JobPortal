from django.shortcuts import render,redirect
from .models import*
from random import randint
from django.db.models import Count
from utils.view_cache import cache_page_view
from django.contrib import messages

# Create your views here.
def IndexView(request):
    return render(request,"index.html")

def LoginView(request):
    return render(request,"login.html")

def SignupPage(request):
    return render(request,"signup.html")

'''
def RegisterUser(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        Email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=Email)
        if user:
            message = "User already Exist"
            return render(request,"signup.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=Email,password=password)
                newcand = Candidate.objects.create(user_id=newuser,firstname=firstname,lastname=lastname)
                return render(request,"otpverify.html",{'email':Email})
    else:
        # Company Registration Code
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        role = request.POST['role']
        company_name = request.POST['company_name']
        company_email = request.POST['email']
        company_password = request.POST['password']
        company_cpassword = request.POST['cpassword']
        user = UserMaster.objects.filter(email=company_email)
        if user:
            message = "Company already Exist"
            return render(request, "signup.html", {'msg': message})
        else:
            if company_password == company_cpassword:
                otp = randint(100000, 999999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=company_email, password=company_password)
                newcompany = Company.objects.create(user_id=newuser,firstname=firstname,lastname=lastname,company_name=company_name)
                return render(request, "otpverify.html", {'email': company_email})      

  '''

from django.core.mail import send_mail
from django.template.loader import render_to_string

def RegisterUser(request):
    if request.POST['role'] == "Candidate":
        role = request.POST['role']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)
        if user:
            messages.error(request, 'User already exists ')
            return redirect(f'/signuppage/')
        else:
            if password == cpassword:
                otp = randint(100000, 999999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                newcand = Candidate.objects.create(user_id=newuser, firstname=firstname, lastname=lastname)

                # Send OTP via Email
                subject = 'OTP Verification'
                message =str(otp)
                from_email = 'ajaysupekar76@gmail.com'  # Update with your email
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list)

                return render(request,"otpverify.html", {'email': email})
    else:
        # Company Registration Code
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        role = request.POST['role']
        company_name = request.POST['company_name']
        company_email = request.POST['email']
        company_password = request.POST['password']
        company_cpassword = request.POST['cpassword']
        user = UserMaster.objects.filter(email=company_email)
        if user:
            messages.error(request, 'Company already exists ')
            return redirect(f'/signuppage/')
        else:
            if company_password == company_cpassword:
                otp = randint(100000, 999999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=company_email, password=company_password)
                newcompany = Company.objects.create(user_id=newuser, firstname=firstname, lastname=lastname, company_name=company_name)

                # Send OTP via Email
                subject = 'OTP Verification'
                message = "Your OTP code is " + str(otp) + ". Please use this to complete your verification."
                from_email ='ajaysupekar76@gmail.com'  # Update with your email
                recipient_list = [company_email]
                send_mail(subject, message, from_email, recipient_list)

                return render(request,"otpverify.html", {'email': company_email})



def OTPPage(request):
    return render(request,"otpverify.html")          
        

def OtpVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)
    if user:
        if user.otp == otp:
            message = "Otp Verify Successfully"
            return render(request,"login.html",{'msg':message})
        else:
            message = "Otp is incorrect"
            return render(request,"otpverify.html",{'msg':message})
    else:
        return render(request,"signup.html")
    
#def ForgotPage(request):
    #return render(request,"forgot.html")




    #############################################################

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

'''
def ForgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = UserMaster.objects.filter(email=email).first()
        if user:
            # Generate token for password reset
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            # Build reset password link
            reset_password_link = request.build_absolute_uri(
                reverse('reset_password', kwargs={'uidb64': uid, 'token': token})
            )

            # Send reset password link via email
            subject = 'Password Reset Link'
            message = render_to_string('email/password_reset_email.html', {
                'reset_password_link': reset_password_link
            })
            from_email = 'ajaysupekar76@gmail.com'  # Your email address
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'A password reset link has been sent to your email.')
            return redirect('loginpage')  # Redirect to login page after sending email
        else:
            messages.error(request, 'No user found with this email address.')
            return redirect('forgotpasswordpage')  # Redirect back to forgot password page if user not found
    return render(request, 'forgot.html')

'''

# views.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse


User = get_user_model()
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)

token_generator = TokenGenerator()

def ForgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = UserMaster.objects.filter(email=email).first()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            reset_password_url = reverse('reset_password', args=[uid, token])
            reset_password_link = request.build_absolute_uri(reset_password_url)

            html_content = render_to_string('reset_password_email.html', {'reset_password_link': reset_password_link})

            subject = 'Password Reset Link'
            from_email = 'ajaysupekar76@gmail.com'
            to_email = email

            msg = EmailMultiAlternatives(subject, '', from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")

            msg.send()

            messages.success(request, 'A password reset link has been sent to your email.')
            return redirect('loginpage')
        else:
            messages.error(request, 'No user found with this email address.')
            return redirect('forgotpasswordpage')
    return render(request, 'forgot.html')


def reset_password(request, uidb64, token):
    context = {
        'uidb64': uidb64,
        'token': token
    }

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserMaster.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserMaster.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')

            if new_password == confirm_new_password:
                # Assign the plain-text password directly to the password field
                user.password = new_password
                user.save()
                messages.success(request, 'Your password has been reset successfully.')
                return redirect('loginpage')
            else:
                messages.error(request, 'Passwords do not match.')
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('forgotpasswordpage')

    return render(request, 'reset_password.html', context)

### auto


#########################################################




'''
def LoginUser(request):
    if request.POST['role']=="Candidate":
        Email = request.POST['email']
        password = request.POST['password']
        user = UserMaster.objects.get(email=Email)
        print(user)
        if user:
            if user.password==password and user.role=="Candidate":
                can=Candidate.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['role']=user.role
                request.session['firstname']=can.firstname
                request.session['lastname']=can.lastname
                request.session['email']=user.email
                return redirect('indexpage')
            else:
                message = "Password does not match"
                return render(request,"login.html",{'msg':message})
        else:
            message = "User doesnot exist"
            return render(request,"login.html",{'msg':message})
'''

'''
def LoginUser(request00):
    role = request.POST.get('role')
    Email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = UserMaster.objects.get(email=Email, role=role)
        if user.password == password:
            if role == "Candidate":
                candidate = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = candidate.firstname
                request.session['lastname'] = candidate.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('indexpage')
            elif role == "Company":
                company = Company.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = company.firstname
                request.session['lastname'] = company.lastname
                request.session['company_name'] = company.company_name
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('companyindex')  # Change 'indexpage' to the appropriate URL for the company dashboard
        else:
            message = "Password does not match"
            return render(request, "login.html", {'msg': message})
    except UserMaster.DoesNotExist:
        message = "User does not exist"
        return render(request, "login.html", {'msg': message})


'''

@cache_page_view(timeout=300)
def LoginUser(request):
    role = request.POST.get('role')
    Email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        if role == "Admin":
            if Email == "admin@gmail.com" and password == "admin@12345":
                request.session['email'] = Email
                request.session['password'] = password
                return redirect(f'/adminindexpage/')
            else:
                messages.error(request, 'Password and email  does not match! ')
                return redirect(f'/loginpage/')
        else:
            user = UserMaster.objects.get(email=Email, role=role)
           
            if user.password == password:
                if role == "Candidate":
                    candidate = Candidate.objects.get(user_id=user)
                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['firstname'] = candidate.firstname
                    request.session['lastname'] = candidate.lastname
                    request.session['email'] = user.email
                    request.session['password'] = user.password
                    return redirect('indexpage')
                elif role == "Company":
                    company = Company.objects.get(user_id=user)
                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['firstname'] = company.firstname
                    request.session['lastname'] = company.lastname
                    request.session['company_name'] = company.company_name
                    request.session['email'] = user.email
                    request.session['password'] = user.password
                    return redirect('companyindex')  # Change 'indexpage' to the appropriate URL for the company dashboard
            else:
              
                messages.error(request, 'Password does not match ! ')
                return redirect(f'/loginpage/')

               
    except UserMaster.DoesNotExist:
        messages.error(request, 'User does not exist !')
        return redirect(f'/loginpage/')



def ProfilePage(request,pk):
    if pk:
        user = UserMaster.objects.get(pk=pk)
        can = Candidate.objects.get(user_id=user)
        return render(request,"profile.html",{'user':user,'can':can})

@cache_page_view(timeout=300)
def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.contact = request.POST['contact']
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.address= request.POST['address']
        can.dob = request.POST['dob']
        can.gender = request.POST['gender']
        can.profile_pic = request.FILES['profile_pic']
        can.save()
        url = f'/profilepage/{pk}'
        return redirect(url)


def ApplyCandidate(request,pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
        return render(request,"apply.html",{'user':user,'cand':cand,'job':job})


def SubmitApplyDetails(request,pk):
    user =request.session['id']
    cand = Candidate.objects.get(user_id=user)
    job = JobDetails.objects.get(id=pk)
    education = request.POST['education']
    experience= request.POST['experience']
    portfoliowebsite = request.POST['portfoliowebsite']
    minimumsalary = request.POST['minimumsalary']
    maximumsalary = request.POST['maximumsalary']
    resume= request.FILES['resume']
    newapply = ApplyList.objects.create(candidate_id=cand,job_id=job,education=education,experience=experience,portfoliowebsite=portfoliowebsite,
                                      minimumsalary=minimumsalary,maximumsalary=maximumsalary,resume=resume)
 
    messages.success(request, 'Job Applied Successfully ! ')
    return redirect(f'/applycandidate/{pk}')


# To Count The Number Of Users Register and Number of Company and posted job and login and display count to the
from django.http import JsonResponse
@cache_page_view(timeout=300)
def Count_User_Company(request):
    # Count the number of users
    user_count = Candidate.objects.count()
    
    # Count the number of companies
    company_count = Company.objects.count()
    job_post = JobDetails.objects.count()
    # Create a JSON response with the counts
    data = {
        'user_count': user_count,
        'company_count': company_count,
        'job_post':job_post
    }
    
    # Return the JSON response
    return JsonResponse(data)



def About(request):
    return render(request,"about.html")

def Contact(request):
    return render(request,"contact.html")
###########################Company Model#####################################################
    
def  CompanyIndexPage(request):
    return render(request,"company/index.html")
    
def CompanyProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    company = Company.objects.get(user_id=user)
    return render(request,"company/profile.html",{'user':user,'company':company})


@cache_page_view(timeout=300)
def UpdateCompanyProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        company = Company.objects.get(user_id=user)
        company.contact = request.POST['contact']
        
        company.state = request.POST['state']
        company.city = request.POST['city']
        company.address= request.POST['address']
        company.website = request.POST['website']
        company.logo_pic = request.FILES['logo_pic']
        company.description = request.POST['description']
        company.save()
        url = f'/companyprofilepage/{pk}'
        return redirect(url)


@cache_page_view(timeout=300)
def JobPostPage(request):
    return render(request,"company/jobpost.html")


def JobDetailSubmit(request):
    user1 = request.session.get('id')
    user = UserMaster.objects.get(id=user1)

    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress = request.POST['companyaddress']
        jobdescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        location = request.POST['location']
        companyemail = request.POST['email']
        companycontact = request.POST['contact']
       
        salarypackage = request.POST['salarypackage']
        experience = request.POST['experience']
        company_logo = request.FILES['company_logo']
        company_website = request.POST['website']
        vacancy = request.POST['vacancy']
        application_deadline = request.POST['application_deadline']
        published_date = request.POST['published_date']
        gender = request.POST['gender']
        newuser = JobDetails.objects.create(company_id=comp,jobname=jobname,companyname=companyname,companyaddress=companyaddress,jobdescription=jobdescription,qualification=qualification,
                                            responsibilities=responsibilities,location=location,companyemail=companyemail,companycontact=companycontact,salarypackage=salarypackage,
                                            experience=experience,company_logo=company_logo,company_website=company_website,vacancy=vacancy,application_deadline=application_deadline,
                                            gender=gender,published_date=published_date)
        message = "Job post Successfully !"
        return render(request,"company/jobpost.html",{'msg':message})
    

###  Company Side to show the Company posting deatils ###
def JobPostListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"company/jobpostlist.html",{'alljob':all_job})

##### candidate side to show the  Job Post List for copany #######
@cache_page_view(timeout=300)
def CandidateJobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"job-listings.html",{'alljob':all_job})


'''
def JobSinglePage(request):
    all_job = JobDetails.objects.all()
    return render(request,"job-single.html",{'alljob':all_job})

'''


def JobSinglePage(request, pk):
    # Retrieve the job detail with the given job_id or return a 404 error if not found
    job = JobDetails.objects.get( pk=pk)
    return render(request, "job-single.html", {'job': job})



@cache_page_view(timeout=300)
# to  search a  company or jobname  but i need to create another page jobsearchpage.html that page show the pertucular job deatails
def Job_Search(request):
    if request.method == 'POST':
        search_company = request.POST.get('search_company')
        if search_company:
            search = JobDetails.objects.filter(search_company=search_company)
            return render(request, 'searchjobpage.html', {'search': search})
        

def CompanyLogout(request):
    del request.session['email']
    del request.session['password']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['company_name']
    return redirect('indexpage')
    

def CandidateLogOut(request):
    del request.session['email']
    del request.session['password']
    del request.session['firstname']
    del request.session['lastname']
    return redirect('indexpage')

def AdminLogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('indexpage')

def JobApplyList(request):
    all_jobapply = ApplyList.objects.all()
    return render(request,"company/applyjoblist.html",{'alljob':all_jobapply})




######################## Admin Side ###########################################


def AdminIndexPage(request):
    if 'email' in request.session and 'password' in request.session:
        return render(request,"admins/index.html")
    else:
        return redirect(f'/loginpage/')

    

def AdminUserList(request):
    all_user = UserMaster.objects.filter(role="Candidate")
    return render(request,"admins/adminuserlist.html",{'alluser':all_user})



def AdminCompanyList(request):
    all_company = UserMaster.objects.filter(role="Company")
    return render(request,"admins/admincompanylist.html",{'allcompany':all_company})

'''
def UserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('adminuserlist')
'''
from django.conf import settings
import os

from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
import os

def UserDelete(request, pk):
    user = get_object_or_404(UserMaster, pk=pk)
    
    # Check if the candidate exists
    try:
        candidate = Candidate.objects.get(user_id=user.pk)
    except Candidate.DoesNotExist:
        # If candidate does not exist, just delete the user and return
        user.delete()
        return redirect('adminuserlist')
    
    # Check if the user has an associated profile picture
    if candidate.profile_pic:
        # Get the path to the profile picture
        image_path = os.path.join(settings.MEDIA_ROOT, str(candidate.profile_pic))

        # Check if the file exists and delete it
        if os.path.exists(image_path):
            os.remove(image_path)

    # Delete the candidate object
    candidate.delete()

    # Delete the user object
    user.delete()

    return redirect('adminuserlist')


def CompnayDelete(request, pk):
    user = get_object_or_404(UserMaster, pk=pk)
    
    # Check if the company exists
    try:
        company = Company.objects.get(user_id=user.pk)
    except Company.DoesNotExist:
        # If company does not exist, just delete the user and return
        user.delete()
        return redirect('adminuserlist')
    
    # Check if the user has an associated profile picture
    if company.logo_pic:
        # Get the path to the profile picture
        image_path = os.path.join(settings.MEDIA_ROOT, str(company.logo_pic))

        # Check if the file exists and delete it
        if os.path.exists(image_path):
            os.remove(image_path)

    # Delete the company object
    company.delete()

    # Delete the user object
    user.delete()

    return redirect('adminuserlist')




def CompanyVerifyPage(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render(request,"admins/verify.html",{'pk':pk})


def ComapnyVerify(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verify=request.POST['verify']
        company.save()
        return redirect('admincompanylist')

    
