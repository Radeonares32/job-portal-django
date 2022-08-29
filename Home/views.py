from django.shortcuts import render
from User.models import Student, Business, Post
from django.shortcuts import render, HttpResponseRedirect, reverse


def index(request):
    post = Post.objects.all().order_by()[:5]
    if request.user.is_authenticated:
        if request.user.is_Student:
            student = Student.objects.filter(user__email=request.user.email).get()
            post_control = Post.objects.filter(students__user__email=request.user.email)

            return render(request, 'index.html',
                          context={'slug': student.slug, 'post': post, 'post_control': post_control})
        elif request.user.is_Business:
            business = Business.objects.filter(user__email=request.user.email).get()
            context = {
                'slug': business.slug,
                'post': post
            }
            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html', context={'post': post})
    else:
        return render(request, 'index.html', context={'post': post})


def companies(request):
    post = Post.objects.all()
    if request.user.is_authenticated:
        if request.user.is_Student:
            student = Student.objects.filter(user__email=request.user.email).get()
            post_control = Post.objects.filter(students__user__email=request.user.email)

            return render(request, 'companies.html',
                          context={'slug': student.slug, 'post': post, 'post_control': post_control})
        elif request.user.is_Business:
            business = Business.objects.filter(user__email=request.user.email).get()
            context = {
                'slug': business.slug,
                'post': post
            }
            return render(request, 'companies.html', context)
        else:
            return render(request, 'companies.html', context={'post': post})
    else:
        return render(request, 'companies.html', context={'post': post})


def companies_detail(request,id):
    post = Post.objects.filter(id=id)
    if request.user.is_authenticated:
        if request.user.is_Student:
            student = Student.objects.filter(user__email=request.user.email).get()
            post_control = Post.objects.filter(students__user__email=request.user.email)

            return render(request, 'company-detail.html',
                          context={'slug': student.slug, 'post': post, 'post_control': post_control})
        elif request.user.is_Business:
            business = Business.objects.filter(user__email=request.user.email).get()
            context = {
                'slug': business.slug,
                'post': post
            }
            return render(request, 'company-detail.html', context)
        else:
            return render(request, 'company-detail.html', context={'post': post})
    else:
        return render(request, 'company-detail.html', context={'post': post})


def companies_list(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Post.objects.filter(title__contains=search)
        if request.user.is_authenticated:
            if request.user.is_Student:
                student = Student.objects.filter(user__email=request.user.email).get()
                post_control = Post.objects.filter(students__user__email=request.user.email)

                return render(request, 'companies-filter.html',
                          context={'slug': student.slug, 'post': post, 'post_control': post_control})
            elif request.user.is_Business:
                business = Business.objects.filter(user__email=request.user.email).get()
                context = {
                'slug': business.slug,
                'post': post
            }
                return render(request, 'companies-filter.html', context)
            else:
                return render(request, 'companies-filter.html', context={'post': post})
        else:
            return render(request, 'companies-filter.html', context={'post': post})