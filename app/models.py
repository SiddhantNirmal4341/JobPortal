from django.db import models
# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

    
class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to="img/candidate")


class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    logo_pic = models.ImageField(upload_to="img/company")
    website = models.URLField(blank=True, null=True)  # Add website field
    description = models.TextField(blank=True, null=True)  # Add description field

    
        

class JobDetails(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250)
    jobdescription = models.CharField(max_length=800)
    qualification = models.CharField(max_length=250)
    responsibilities = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    companyemail = models.CharField(max_length=250)
    companycontact = models.CharField(max_length=20)
    salarypackage = models.CharField(max_length=250)
    experience = models.IntegerField()
    company_logo = models.ImageField(upload_to="img/company/jobpost")
    company_website = models.URLField(blank=True, null=True)  # Add website field
    vacancy = models.IntegerField()
    published_date = models.CharField(max_length=50)
    application_deadline = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)




class ApplyList(models.Model):
    candidate_id = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job_id =  models.ForeignKey(JobDetails,on_delete=models.CASCADE)
    education = models.CharField(max_length=250)
    portfoliowebsite = models.CharField(max_length=250)
    minimumsalary = models.CharField(max_length=250)
    maximumsalary =models.CharField(max_length=250)
    resume = models.FileField(upload_to="app/resume")
    experience =models.IntegerField(default=2)




    



