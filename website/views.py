from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            form.save()
            # Save the data to the database or send an email, etc.
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent successfully!')
        else:
            # Return an error response
            messages.add_message(request, messages.ERROR, 'There was an error sending your message. Please try again.')
    form = ContactForm()  # Reinitialize the form to clear the data after processing
    return render(request, 'website/contact.html',{'form': form})


def test_view(request):
    form = NameForm()  # Initialize the form with no data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            form.save()
            # Save the data to the database or send an email, etc.
            # Return a success response
            # print("Form is valid")
            return HttpResponse("Form is valid")
        else:
            # Return an error response
            return HttpResponse("Form is not valid")
    form = ContactForm()  # Reinitialize the form to clear the data after processing    
    return render(request, 'test.html',{'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            form.save()
            # Save the data to the database or send an email, etc.
            return HttpResponseRedirect('/')
    else:   
        return HttpResponseRedirect('/')
