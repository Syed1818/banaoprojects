# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# We only need this import once
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from .models import Profile

def signup_view(request):
    if request.user.is_authenticated:
        # If user is already logged in, redirect them
        if request.user.profile.user_type == 'doctor':
            return redirect('doctor_dashboard')
        return redirect('patient_dashboard')

    if request.method == 'POST':
        # Pass POST data and FILES data (for the image) to the form
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            
            # Create the User object
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            
            # Create the Profile object linked to the user
            profile = Profile.objects.create(
                user=user,
                profile_picture=data['profile_picture'],
                address_line1=data['address_line1'],
                city=data['city'],
                state=data['state'],
                pincode=data['pincode'],
                user_type=data['user_type']
            )
            
            # Log the user in
            login(request, user)
            
            # Redirect to the correct dashboard
            if profile.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    else:
        form = SignUpForm()
        
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        # If user is already logged in, redirect them
        if request.user.profile.user_type == 'doctor':
            return redirect('doctor_dashboard')
        return redirect('patient_dashboard')

    if request.method == 'POST':
        # Use our custom LoginForm
        form = LoginForm(request, data=request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Redirect based on user type
                if user.profile.user_type == 'doctor':
                    return redirect('doctor_dashboard')
                else:
                    return redirect('patient_dashboard')
    else:
        # Use our custom LoginForm
        form = LoginForm() 
        
    return render(request, 'users/login.html', {'form': form})

@login_required
def patient_dashboard(request):
    # Ensure only patients can access this page
    if request.user.profile.user_type != 'patient':
        return redirect('doctor_dashboard') # Or a 403 forbidden page
    
    profile = request.user.profile
    return render(request, 'users/dashboard.html', {'profile': profile})

@login_required
def doctor_dashboard(request):
    # Ensure only doctors can access this page
    if request.user.profile.user_type != 'doctor':
        return redirect('patient_dashboard') # Or a 403 forbidden page
        
    profile = request.user.profile
    return render(request, 'users/dashboard.html', {'profile': profile})

def logout_view(request):
    logout(request)
    return redirect('login')