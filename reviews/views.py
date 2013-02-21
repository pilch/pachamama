from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from reviews.models import Person, PersonForm, Review, ReviewForm, UserCreateForm, SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import account.views


class SignupView(account.views.SignupView):

   form_class = SignupForm

   def after_signup(self, form):
       self.create_profile(form)
       super(SignupView, self).after_signup(form)

   def create_profile(self, form):
       profile = self.created_user.get_profile()
       profile.birthdate = form.cleaned_data["birthdate"]
       profile.save()

def register(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            #lastname = form.cleaned_data['last_name']
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            university = form.cleaned_data['university']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username,password)
            user.save()
            p = Person(first_name = firstname, last_name = lastname, university = uni,email = email)
            p.save()
    else:  
        form = PersonForm()

    return render(request,'reviews/register.html',{
              'form': form,
              })
    
def login_view(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            #Log them in - don't redirect to new page shit is sloppy
        else:
            return#disabled error message
    else:
        return#invalid login - change password or something page