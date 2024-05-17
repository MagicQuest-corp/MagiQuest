from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView
from .models import Mission
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(ListView):
    model = Mission
    template_name = 'authentication/index.html'

    

class MissionView(DetailView):
    model = Mission 
    template_name = 'authentication/mission_details.html'
    

class AddMissionView(LoginRequiredMixin, CreateView):
    model = Mission
    template_name = 'authentication/mission_post.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogSearchView(ListView):
    model = Mission
    template_name = 'index.html'
    context_object_name = 'missions'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Mission.objects.filter(title__icontains=query).order_by('-created_at')
        else:
            return Mission.objects.none()

def about(request):
    return render(request, "authentication/about.html") 

def contact_us(request):
    return render(request, "authentication/contact_us.html")

def home(request):
    return render(request, "authentication/signin.html")

def signup(request):
    if request.method == "POST":
        username= request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some other username")
            return redirect('signin')

        if User.objects.filter(email=email):
            messages.error(request,"Email already registered!")
            return redirect('signin')

        if pass1 != pass2:
            messages.error (request, "Password didn't match!")
            return redirect('signin')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created")

        return redirect('signin')


    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return redirect('LandingPage')

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('signin')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('signin')