# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from .models import Profile


# ... (signup_view is unchanged)
def signup_view(request):
    # ... (same as before)
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        if request.user.profile.user_type == 'doctor':
            return redirect('doctor_dashboard')
        return redirect('patient_dashboard')

    if request.method == 'POST':
        # --- CHANGE THIS LINE ---
        form = LoginForm(request, data=request.POST) # Use our custom LoginForm
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                if user.profile.user_type == 'doctor':
                    return redirect('doctor_dashboard')
                else:
                    return redirect('patient_dashboard')
    else:
        # --- AND CHANGE THIS LINE ---
        form = LoginForm() # Use our custom LoginForm
        
    return render(request, 'users/login.html', {'form': form})

# ... (dashboard and logout views are unchanged)
def logout_view(request):
    logout(request)
    return redirect('login')