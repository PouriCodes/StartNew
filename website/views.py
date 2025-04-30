from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.models import Contact
from website.forms import NameForm

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    return render(request, 'website/contact.html')


def test_view(request):
    form = NameForm()  # Initialize the form with no data
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save the data to the database or send an email, etc.
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()

            # Return a success response
            print("Form is valid")
        else:
            # Return an error response
            return HttpResponse("Form is not valid")
        
    return render(request, 'test.html',{'form': form})

