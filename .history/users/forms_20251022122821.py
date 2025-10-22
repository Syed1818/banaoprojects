from django import forms
from .models import Profile
from django.contrib.auth.models import User
# Import the default login form
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(forms.Form):
    # ... (all your fields are the same)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    profile_picture = forms.ImageField(required=True)
    address_line1 = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    pincode = forms.CharField(max_length=6, required=True)
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES, required=True)

    # --- ADD THIS __init__ METHOD ---
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Loop through all fields and add the 'form-control' class
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            # Special case for the profile picture (file input)
            if field_name == 'profile_picture':
                field.widget.attrs['class'] = 'form-control form-control-sm'
            # Special case for the user_type (select dropdown)
            if field_name == 'user_type':
                field.widget.attrs['class'] = 'form-select'

    # ... (all your 'clean' methods are the same)
    def clean_username(self):
        # ... (same as before)
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        # ... (same as before)
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean(self):
        # ... (same as before)
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")


# --- ADD THIS NEW LOGIN FORM ---
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Add 'form-control' to username and password fields
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'