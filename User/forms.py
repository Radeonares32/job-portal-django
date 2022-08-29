from django import forms
from .models import Student, Business, CustomUser, Post


class StudentRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    last_name = forms.CharField(max_length=100, label='First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    email = forms.CharField(max_length=100, label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'type': 'password'}),
                                label='Password')
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'type': 'password'}), label='Password Repeat')


class BusinessRegisterForm(forms.Form):
    email = forms.CharField(max_length=100, label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    business_name = forms.CharField(max_length=100, label='Business Name',
                                    widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    first_name = forms.CharField(max_length=100, label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    last_name = forms.CharField(max_length=100, label='First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'type': 'password'}))
    password_repeat = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'type': 'password'}))


class StudentLoginForm(forms.Form):
    email = forms.CharField(max_length=100, label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'type': 'password'}))


class BusinessLoginForm(forms.Form):
    email = forms.CharField(max_length=100, label='Email',
                            widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'type': 'password'}))


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('image', 'phone', 'about', 'skills', 'university', 'department', 'grade_average', 'classes')
        exclude = ('slug', 'user')

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'about': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'skills': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'university': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'department': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'grade_average': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'classes': forms.TextInput(attrs={'class': 'form-control input-lg'}),
        }


class BusnissProfileForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('image', 'phone', 'about', 'gmail_password')
        exclude = ('business_name', 'posts', 'slug')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'about': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'gmail_password': forms.TextInput(attrs={'class': 'form-control input-lg'}),
        }


class PostAdd(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control input-lg'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))


class PostUpdate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'address', 'description', 'tags')
        exclude = ('slug', 'students')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'address': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control input-lg'}),
            'tags': forms.TextInput(attrs={'class': 'form-control input-lg'}),
        }
