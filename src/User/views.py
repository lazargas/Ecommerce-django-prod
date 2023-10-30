from django.shortcuts import render,redirect
from .forms import SignInForm,SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
import re
# Create your views here.

pattern = r'^([^@]+)@'
def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST['password']
            match = re.match(pattern, email)
            username=match.group(1)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or any desired URL after successful login
                return redirect('/')
            else:
                # Invalid username or password
                form.add_error(None, 'Invalid username or password')
    else:
        form = SignInForm()

    return render(request, 'auth.html', {'form': form})

def signup_view(request):
    context={}
    form = SignUpForm(request.POST or None)
    if request.method=="POST":
        email = request.POST["email"]
        password = request.POST["password"]
        match = re.match(pattern, email)
        if match:
           username=match.group(1)
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/User/signin')
    return render(request,"signup.html")


def signout_view(request):
    logout(request)
    return redirect("/")
    
    

    
          
     
    
