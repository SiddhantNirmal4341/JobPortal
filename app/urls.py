from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.IndexView,name="indexpage"),
    path("aboutpage/",views.About,name="aboutpage"),
    path("contact/",views.Contact,name="contact"),
    path("loginpage/",views.LoginView,name="loginpage"),
    path("signuppage/",views.SignupPage,name="signuppage"),
    path("regiter/",views.RegisterUser,name="regiter"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otp/",views.OtpVerify,name="otp"),
    path("loginuser/",views.LoginUser,name="loginuser"),
    path("profilepage/<int:pk>",views.ProfilePage,name="profilepage"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
    path("candidatelogout/",views.CandidateLogOut,name="candidatelogout"),
    path("candidatejobpostlist/",views.CandidateJobListPage,name="candidatejobpostlist"),
    path("jobsinglepage/<int:pk>",views.JobSinglePage,name="jobsinglepage"),
    path("applycandidate/<int:pk>",views.ApplyCandidate,name="applycandidate"),
    path("submitapplydetails/<int:pk>",views.SubmitApplyDetails,name="submitapplydetails"),
    path("countusercompany/",views.Count_User_Company,name="countusercompany"),

    path("forgotpasswordpage/",views.ForgotPassword,name="forgotpasswordpage"),
    path('reset_password/<str:uidb64>/<str:token>/', views.reset_password, name='reset_password'),

    path("jobsearchpage/",views.Job_Search,name="jobsearchpage"),
   # path("jobsearch/",views.Job_Search,name="jobsearch"),

    
    ##########################Company Model Urls##########################################
    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("companyprofilepage/<int:pk>",views.CompanyProfilePage,name="companyprofilepage"),
    path("updatecompany/<int:pk>",views.UpdateCompanyProfile,name="updatecompany"),
    path("jobpostpage/",views.JobPostPage,name="jobpostpage"),
    path("jobdetailsubmit/",views.JobDetailSubmit,name="jobdetailsubmit"),
    path("jobpostlistpage/",views.JobPostListPage,name="jobpostlistpage"),
    path("companylogout/",views.CompanyLogout,name="companylogout"),
    path("jobapplylist/",views.JobApplyList,name="jobapplylist"),
    

    ########################### Admin site ##############################################
    #path("adminloginpages/",views.AdminLoginPage,name="adminloginpages"),
    path("adminindexpage/",views.AdminIndexPage,name="adminindexpage"),

    #path("adminlogin/",views.AdminLogin,name="adminlogin"),
    path("adminuserlist/",views.AdminUserList,name="adminuserlist"),
    path("admincompanylist/",views.AdminCompanyList,name="admincompanylist"),

    path("userdelete/<int:pk>",views.UserDelete,name="userdelete"),
    path("companydelete/<int:pk>",views.CompnayDelete,name="companydelete"),
    path("companyverifypage/<int:pk>",views.CompanyVerifyPage,name="companyverifypage"),
    path("companyverify/<int:pk>",views.ComapnyVerify,name="companyverify"),
    path("adminlogoutpage/",views.AdminLogout,name="adminlogoutpage")

]


if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
