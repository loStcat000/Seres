from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Profile


from .forms import SignUpForm

@login_required
def changepassword(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            # Check if old password is correct
            old_password = password_form.cleaned_data.get('old_password')
            if not request.user.check_password(old_password):
                password_form.add_error('old_password', 'Incorrect old password.')
            else:
                # Save new password and redirect
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_form = PasswordChangeForm(user=request.user)
    return render(request, 'profile.html', {'password_form': password_form})


#registration function

def signup_request(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, "This email is already registered.")
            else:
                user = form.save(commit=False)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                user.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()
    return render(request=request, template_name="signup.html", context={"register_form": form})




#login function
from django.contrib import messages

def login_request(request):
    
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                else:
                    messages.error(request, "Your account is inactive.")
            else:
                messages.error(request, "Invalid username or password.")
            return redirect('home')
        else:
            return render(request, "login.html", context={})



#logout function
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login')


def profile(request, pk): 
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)        
        return render(request, "profile.html", {"profile":profile})
    else:
        messages.success(request, ("You Must Be logged In!!"))
        return redirect('login')