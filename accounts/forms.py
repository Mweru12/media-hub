# is an app that helps with form management that is how you capture details from your form and what sort of validations go with those particular details you are capturin
# to utilize the forms we go ahead and import from django 
# extend the django's auth form
# UserCreationForm for signup, AuthenticationForm is for log in, PasswordResetForm for password resets
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import User

# this is the registration form
class UserRegistrationForm(UserCreationForm):
    # email field for validation setup
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class' : 'form-control',
                                                                            'placeholder' : 'Email' }))
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, widget=forms.Select(attrs={
        'class' : 'form-control'
    }))
    # the above is for extending the behavviour of the already inputs eg the email, user_type
    class Meta: # more informtion about this form 
        model = User
        fields = ('username', 'email', 'user_type', 'password1', 'password2') # simply the form fields my user will fill
        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            })
        } # defines what i want for my username

        #passwords
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'password'}) 
            self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm Password'})

# login form 
class UserLoginForm(AuthenticationForm): # this class inherits from the AuthenticationForm
    username = forms.CharField(widgets=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    password = forms.CharField(widgets=forms.PasswordInput(attrs={
        'class':'form-control', # form-control is a styling class
        'placeholder':'Password'
    }))

# profile form : update an account profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','bio','profile_image')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control','rows': 3})
        }