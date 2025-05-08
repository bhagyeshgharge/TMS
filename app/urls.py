from django.urls import path
from app import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name="home"),
    path('login',views.Login,name="login"),
    path('SignUp',views.Signup,name="SignUp"),
    path('logout', views.LogOut, name='logout'),
    path('All_packages',views.Packages, name="All_packages"),
    path('send_otp',views.send_otp,name="send_otp"),
    path('add_package',views.Add_package,name="add_package"),
    path('package_deatils/<int:pid>/', views.Package_details, name='package_details'),
    # path('package_details/<pid>',views.pa, name="package_details"),
    # path('package-trending/', views.package_trending, name="package_trending"),  # New route for trending packages
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)