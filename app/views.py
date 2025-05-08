from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserRegistrationForm
from.models import *
import json
from app.models import CustomUser  # Import your CustomUser model
from .utils import *  # Import the functionimport time
from .utils import generate_and_send_otp, verify_otp



# Create your views here.

def home(request):
    trending_packages = Package.objects.filter(is_active=True, is_trending=True)
    explore_packages = Package.objects.filter(is_active=True)[:10]  # Limit to 10 packages
    return render(request, "home.html", {
        "customuser": request.user,
        "trending_packages": trending_packages,
        "explore_packages": explore_packages
    })

def Header(request):
    context = {}
    if request.user.is_authenticated:
        context["customuser"] = request.user  # Pass user object to template
    return render(request, "header.html", context)

# def pa(request,pid):
#     return render(request,'Packages_Details.html')

def Login(request):
    error_message = None

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
            authenticated_user = authenticate(request, username=user.email, password=password)

            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')
            else:
                error_message = 'Invalid email or password. Please try again.'

        except CustomUser.DoesNotExist:
            error_message = 'No account found with this email.'

    return render(request, 'LogIn.html', {'error_message': error_message})
    


"""
def Signup(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Do not save to the database yet
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user to the database
            return render(request, 'SignUp.html', {'form': CustomUserRegistrationForm(), 'account_created': True})
        else:
            messages.error(request, 'There was an error with your registration. Please check your input.')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'SignUp.html', {'form': form})"""




def Signup(request):
    otp_sent = False  # Track OTP status

    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        action = request.POST.get('action')
        email = request.POST.get('email')

        if action == 'send_otp':
            if email:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already registered. Please use a different email.')
                else:
                    otp_hash, expiry_time = generate_and_send_otp(email)
                    if otp_hash:
                        request.session.update({
                            'otp_email': email,
                            'otp_hash': otp_hash,
                            'otp_expiry_time': expiry_time
                        })
                        otp_sent = True  # ✅ OTP was successfully sent
                        messages.success(request, 'OTP has been sent to your email.')
                    else:
                        messages.error(request, 'Failed to send OTP. Please try again.')
            else:
                messages.error(request, 'Please provide a valid email address to receive the OTP.')

            return render(request, 'SignUp.html', {'form': form, 'otp_sent': otp_sent})  # ✅ Pass to template

        elif action == 'sign_up':
            otp = request.POST.get('otp')

            otp_email = request.session.get('otp_email')
            otp_expiry_time = request.session.get('otp_expiry_time')
            otp_hash = request.session.get('otp_hash')

            if not all([otp_email, otp_expiry_time, otp_hash]):
                messages.error(request, 'OTP verification data is missing. Please request a new OTP.')
            elif email != otp_email:
                messages.error(request, 'The email does not match the one used for OTP generation.')
            elif verify_otp(email, otp, otp_hash, otp_expiry_time):
                if form.is_valid():
                    user = form.save(commit=False)
                    user.set_password(form.cleaned_data['password'])
                    user.is_active = True
                    user.save()

                    login(request, user)
                    messages.success(request, 'Account created successfully! You are now logged in.')

                    for key in ['otp_email', 'otp_hash', 'otp_expiry_time']:
                        request.session.pop(key, None)

                    return redirect('/')
                messages.error(request, 'There was an error with your registration. Please check your input.')
            else:
                messages.error(request, 'Invalid or expired OTP. Please try again.')

    else:
        form = CustomUserRegistrationForm()

    return render(request, 'SignUp.html', {'form': form, 'otp_sent': otp_sent})




def LogOut(request):
     logout(request)
     return redirect('/')



def send_otp(request):
    pass



def Add_package(request):
    if request.method == 'POST':
        # Extract form data
        place = request.POST.get('place')
        country = request.POST.get('country')
        state = request.POST.get('state')
        price = request.POST.get('price')
        days = request.POST.get('days')
        nights = request.POST.get('nights')
        description = request.POST.get('description')
        total_person = request.POST.get('total_person', 1)

        # Boolean Fields: Default `is_active=True`, and `is_trending=False`
        is_active = request.POST.get('activate') == '1'  # Default True
        is_trending = request.POST.get('trending') == '1'  # Default False

        # Handle Image Uploads
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')

        # Handle Start and End Dates
        start_dates = request.POST.getlist('start_date')
        end_dates = request.POST.getlist('end_date')
        months = request.POST.getlist('month_hidden')
        months_str = ",".join(months)

       
        # Save all months in JSON
        months_json = json.dumps(months)

        # Handle Days Plan
        days_plan = []
        for i in range(1, int(days) + 1):
            day_plan = request.POST.get(f'Days_plan_{i}', '')
            days_plan.append(day_plan)

        # Save to Database
        Package.objects.create(
            place=place,
            country=country,
            state=state,
            price=float(price),
            days=int(days),
            nights=int(nights),
            description=description,
            total_person=int(total_person),
            is_active=is_active,
            is_trending=is_trending,
            image1=image1,
            image2=image2,
            image3=image3,
            image4=image4,
            start_dates=start_dates,
            end_dates=end_dates,
            # months=months_json,
            months=months_str,  # Save as comma-separated string
            days_plan=days_plan
        )

        return redirect('/')
    
    context = {'month_choices': Package.MONTH_CHOICES}
    return render(request, 'add_package.html', context)



def Packages(request):  

    packages = Package.objects.filter(is_active=True)  # Only check for is_active
    return render(request, "packages.html", {"customuser": request.user, "packages": packages})
  
    # packages = Package.objects.filter(is_active=True,  is_trending=True)  # Fetch only active packages
    # return render(request, "packages.html", {"customuser": request.user, "packages": packages})



def Package_details(request, pid):
    try:
        package = Package.objects.get(id=pid)
    except Package.DoesNotExist:
        return redirect('/')

    date_cards = []
    for start, end in zip(package.start_dates, package.end_dates):
        date_cards.append({
            'start': start,
            'end': end,
            'price': package.price,
            'days': package.days,
            'nights': package.nights,
            'place': package.place,
            'id': package.id,
        })

    context = {
        'package': package,
        'date_cards': date_cards,
    }
    return render(request, 'Package_details.html', context)
