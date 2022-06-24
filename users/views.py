from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import User
from .forms import *


# Create your views here.
# def register(req):
#     frm = Registerform()
#     context = {}
#     context['form'] = frm
#     frm = Registerform(req.POST)
#     if req.method == 'GET':
#         return render(req, 'users/register.html')
#     else:
#         frm = Registerform(req.POST)
#         if (frm.is_valid()):
#             u=User()
#             u.user_name=req.POST['username']
#             u.passwor = req.POST['password']
#             u.save()
#             User.objects.create(user_name=req.POST['username'], passwor=req.POST['password'], is_staff=True)
#         return render(req, 'users/login.html')


##### register
def register(req):
    frm = Registerform()
    context = {}
    context['form']=frm
    if (req.method == 'GET'):
        # context['form'] = frm
        return render(req, 'users/register.html', context)
    else:
        frm = Registerform(req.POST)
        if (frm.is_valid()):
            u=User()
            u.user_name=req.POST['username']
            u.passwor = req.POST['password']
            u.save()
            # User.objects.create_superuser(user_name=req.POST['username'], passwor=req.POST['password'], is_staff=True)

        return redirect( '/users/login')
#

######### login

def login(request):
    if (request.method == 'GET'):
        return render(request, 'users/login.html', {})
    else:
        user=User.objects.filter(user_name=request.POST['username'], passwor=request.POST['exampleInputPassword'])
        users = authenticate(user_name=request.POST['username'], passwor=request.POST['exampleInputPassword'])

        if (len(user) != 0):
            request.session['loginid'] = user[0].id
            request.session['user_name'] = user[0].user_name
            return redirect('/Trainee/list')
            # return HttpResponse('login')
        else:
            return HttpResponseRedirect('/login')

        # if users is not None:
        #     return redirect('/Trainee/list')
        # else:
        #     return HttpResponseRedirect('/login')
        # return render(req, 'users/login.html', {'error': 'invalid'})




def listview(request):
    request.session.clear()
    if request.user.is_authenticated():
        login(request,HttpResponseRedirect('/list'))
    else:
        redirect('/users/login')