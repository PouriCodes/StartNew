from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea, max_length=500)


class ContactForm(forms.ModelForm):
    captcha = CaptchaField(label='Captcha')
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter subject'}),
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Enter your message'}),
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }
        help_texts = {
            'name': 'Enter your full name.',
            'email': 'Enter a valid email address.',
            'subject': 'Enter the subject of your message.',
            'message': 'Enter your message here.',
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }
        labels = {
            'email': 'Email',
        }
        help_texts = {
            'email': 'Enter a valid email address to subscribe to our newsletter.',
        }