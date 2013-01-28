from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from reviews.models import Person, PersonForm

def register(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            uni = form.cleaned_data['university']
            email = form.cleaned_data['email']
            p = Person(first_name = firstname, last_name = lastname, university = uni,email = email)
            p.save()
    else:  
        form = PersonForm()

    return render(request,'reviews/register.html',{
              'form': form,
              })
    
    
    
    '''
    person_list = Person.objects.all()
    context = {'person_list': person_list}
    return render(request,'reviews/register.html',context)
    '''

