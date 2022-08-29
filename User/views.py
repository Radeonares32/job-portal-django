import os.path
from django.contrib.auth.models import User
from django.contrib.auth import login as Login, logout, authenticate
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.hashers import check_password
from .forms import StudentRegisterForm, StudentLoginForm, BusinessLoginForm, BusinessRegisterForm, StudentProfileForm, \
    BusnissProfileForm, PostAdd, PostUpdate
from .models import Student, Business, CustomUser, Post
from django.contrib.auth import get_user_model


def register(req):
    if req.method == 'GET':
        form = StudentRegisterForm()
        context = {
            'form': form
        }
        return render(req, 'student-register.html', context)
    elif req.method == 'POST':
        form = StudentRegisterForm(req.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                is_exist_user = get_user_model().objects.filter(email=email, username=f'{first_name} {last_name}')
                if is_exist_user.exists():
                    return HttpResponseRedirect('register?message=user_exists')
                else:
                    user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                          password=password1, username=f'{first_name} {last_name}',
                                                          is_Student=True)
                    student = Student.objects.create(user=user, name=first_name)
                    user.save()
                    student.save()
                    return HttpResponseRedirect(reverse('login'))
            else:
                return HttpResponseRedirect('register?message=no_match')
        else:
            return HttpResponseRedirect('register')


def login(request):
    if request.method == 'GET':
        form = StudentLoginForm()
        context = {
            'form': form
        }
        return render(request, 'student-login.html', context)
    elif request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            is_exist_user = CustomUser.objects.filter(email=email)
            if is_exist_user.exists() and check_password(password, is_exist_user.get().password):
                login_user = authenticate(request, username=is_exist_user.get().username, password=password)
                if login_user is not None:
                    Login(request, user=login_user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponseRedirect('login?message=no_user')
        else:
            return HttpResponseRedirect('login?message=unknown')
    else:
        return HttpResponseRedirect('login?message=unknown')


def business_login(req):
    if req.method == 'GET':
        form = BusinessLoginForm()
        context = {
            'form': form
        }
        return render(req, 'businiss-login.html', context)
    elif req.method == 'POST':
        form = BusinessLoginForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            is_exist_user = CustomUser.objects.filter(email=email)
            if is_exist_user.exists() and check_password(password, is_exist_user.get().password):
                login_user = authenticate(req,
                                          username=f'{is_exist_user.get().first_name} {is_exist_user.get().last_name}',
                                          password=password, email=email)
                if login_user is not None:
                    Login(req, user=login_user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponseRedirect('business-login?message=invalid_user')
            else:
                return HttpResponseRedirect('business-login?message=no_user')
        else:
            return HttpResponseRedirect('login?message=unknow')


def business_register(req):
    if req.method == 'GET':
        form = BusinessRegisterForm()
        context = {
            'form': form
        }
        return render(req, 'business-register.html', context)
    elif req.method == 'POST':
        form = BusinessRegisterForm(req.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            business_name = form.cleaned_data['business_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['password_repeat']
            if password == password_repeat:
                is_exist_user = get_user_model().objects.filter(email=email, username=f'{first_name} {last_name}')
                if is_exist_user.exists():
                    return HttpResponseRedirect('business-register?message=user_exists')
                else:
                    user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                          password=password, username=f'{first_name} {last_name}',
                                                          is_Business=True)
                    business = Business.objects.create(user=user, business_name=business_name)
                    user.save()
                    business.save()
                    return HttpResponseRedirect(reverse('business-login'))
            else:
                return HttpResponseRedirect('business-register?message=no_match')
        else:
            return HttpResponseRedirect('business-register')


def Logout(request):
    logout(request=request)
    return HttpResponseRedirect(reverse('home'))


def business_profile(request, slug):
    if request.user.is_authenticated:
        if request.user.is_Business:
            business = Business.objects.filter(user__email=request.user.email).get()
            context = {
                'slug': business.slug,
                'business_name': business.business_name,
                'phone': business.phone,
                'about': business.about,
                'image': business.image.url

            }
            return render(request, 'business-profile.html', context)
    else:
        return HttpResponseRedirect('/?message=not_auth')


def student_profile(request, slug):
    if request.user.is_authenticated:
        if request.user.is_Student:
            student = Student.objects.filter(user__email=request.user.email).get()
            context = {
                'phone': student.phone,
                'slug': student.slug,
                'skills': student.skills,
                'university': student.university,
                'department': student.department,
                'grade_average': student.grade_average,
                'class': student.classes,
                'image': student.image.url,
                'about': student.about
            }
            return render(request, 'student-profile.html', context)
    else:
        return HttpResponseRedirect('/?message=not_auth')


def get_student_profile_edit(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            student = Student.objects.filter(user__email=request.user.email).get()
            students = Student.objects.get(id=student.id)
            form = StudentProfileForm(instance=students)
            context = {
                'phone': student.phone,
                'slug': student.slug,
                'skills': student.skills,
                'university': student.university,
                'department': student.department,
                'grade_average': student.grade_average,
                'class': student.classes,
                'about': student.about,
                'form': form
            }
            return render(request, 'student-profile-update.html', context)
    else:
        return HttpResponseRedirect('/?message=not_auth')


def post_student_profile_edit(request):
    if request.method == 'POST':
        student = Student.objects.filter(user__email=request.user.email)
        student_instance = Student.objects.get(id=student.get().id)
        form = StudentProfileForm(request.POST, request.FILES, instance=student_instance)
        if form.is_valid():
            image_path = student_instance.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
            form.save()
            return HttpResponseRedirect(f'student-profile/{student.get().slug}')
    else:
        return HttpResponseRedirect('student-profile-edit?message=not_invalid')


def get_business_profile_edit(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            business = Business.objects.filter(user__email=request.user.email).get()
            businesses = Business.objects.get(id=business.id)
            form = BusnissProfileForm(instance=businesses)
            context = {
                'slug': business.slug,
                'business_name': business.business_name,
                'phone': business.phone,
                'about': business.about,
                'form': form
            }
        return render(request, 'business-profile-update.html', context)
    else:
        return HttpResponseRedirect('/?message=not_auth')


def post_business_profile_edit(request):
    if request.method == 'POST':
        business = Business.objects.filter(user__email=request.user.email).get()
        businesses = Business.objects.get(id=business.id)
        form = BusnissProfileForm(request.POST, request.FILES, instance=businesses)
        if form.is_valid():
            image_path = businesses.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
            form.save()
            return HttpResponseRedirect(f'business-profile/{business.slug}')
        else:
            return HttpResponseRedirect('business-profile-edit?message=not_invalid')


def get_post(request):
    if request.method == 'GET':
        business = Business.objects.filter(user__email=request.user.email).get()
        form = PostAdd()
        context = {
            'form': form,
            'slug': business.slug
        }
        return render(request, 'business-post-add.html', context)


def post_post(request):
    if request.method == 'POST':
        post_form = PostAdd(request.POST)
        business = Business.objects.filter(user__email=request.user.email)
        if post_form.is_valid():
            title = post_form.cleaned_data['title']
            description = post_form.cleaned_data['description']
            address = post_form.cleaned_data['address']
            tags = post_form.cleaned_data['tags']
            post = Post.objects.create(title=title, description=description, address=address, tags=tags,
                                       businesses=business.get())
            post.save()
            return HttpResponseRedirect('business-post-list')

        else:
            return HttpResponseRedirect('business-post?message=not_invalid')


def post_list(request):
    if request.method == 'GET':
        business = Business.objects.filter(user__email=request.user.email)
        post = Post.objects.filter(businesses__user__email=request.user.email)
        context = {
            'slug': business.get().slug,
            'business': post
        }
        return render(request, 'business-post-list.html', context)


def post_update(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post_form = PostUpdate(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse('business-post-list'))
        else:
            return HttpResponseRedirect('business-post-updates?message=not_invalid')


def get_post_update(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        post_form = PostUpdate(request.POST, instance=post)
        context = {
            'form': post_form,
            'slug': post.slug,
            'id': post.id
        }
        return render(request, 'business-post-update.html', context)


def delete_post(request, id):
    if request.method == 'GET':
        Post.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('business-post-list'))


def student_apply(request, id):
    if request.user.is_authenticated:
        if request.user.is_Student:
            post = Post.objects.filter(id=id)
            student = Student.objects.get(user__email=request.user.email)
            post_control = Post.objects.filter(students=student.id, id=id)
            if post_control.exists():
                return HttpResponseRedirect('/?message=already_apply')
            post.get().students.add(student)
            return HttpResponseRedirect(reverse('student-apply-list'))
        else:
            return HttpResponseRedirect('/?message=no_student_user')
    else:
        return HttpResponseRedirect('/?message=no_auth')


def student_apply_list(request):
    if request.user.is_authenticated:
        post = Post.objects.filter(students__user__email=request.user.email)
        student = Student.objects.filter(user__email=request.user.email).get()
        context = {
            'slug': student.slug,
            'post': post
        }
        return render(request, 'student-apply-list.html', context)


def business_profile_detail(request, slug):
    business = Business.objects.filter(slug=slug)
    if request.user.is_authenticated:
        if request.user.is_Student:
            student = Student.objects.filter(user__email=request.user.email).get()

            return render(request, 'business-profile-detail.html',
                          context={'slug': student.slug, 'business': business})
        elif request.user.is_Business:
            context = {
                'slug': business.get().slug,
                'business': business
            }
            return render(request, 'business-profile-detail.html', context)
        else:
            return render(request, 'business-profile-detail.html',
                          context={'slug': business.get().slug, 'business': business})
    else:
        return render(request, 'business-profile-detail.html',
                      context={'slug': business.get().slug, 'business': business})


def student_profile_detail(request, slug):
    student = Student.objects.filter(slug=slug)
    if request.user.is_authenticated:
        if request.user.is_Student:
            student = Student.objects.filter(user__email=request.user.email).get()

            return render(request, 'student-profile-detail.html',
                          context={'slug': student.slug, 'student': student})
        elif request.user.is_Business:
            context = {
                'slug': student.get().slug,
                'student': student
            }
            return render(request, 'student-profile-detail.html', context)
        else:
            return render(request, 'student-profile-detail.html',
                          context={'slug': student.get().slug, 'student': student})
    else:
        return render(request, 'student-profile-detail.html',
                      context={'slug': student.get().slug, 'student': student})


def business_list_student(request, id):
    if request.user.is_authenticated:
        business = Business.objects.filter(user__email=request.user.email)
        if request.user.is_Business:
            post = Post.objects.filter(id=id)
            context = {
                'slug': business.get().slug,
                'post': post
            }
            return render(request, 'business-post-apply-list.html', context)


