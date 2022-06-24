from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Trainee, Course
from .forms import *
from django.views import View
from django.views.generic import ListView, DetailView

from django.views.generic.edit import UpdateView


# Create your views here.
def list(req):
    trainees = Trainee.objects.all()
    for trainee in trainees:
        print(trainee.id, trainee.name, trainee.courses)
    context = {}
    context['title'] = 'List'
    context['trainees'] = trainees
    return render(req, 'list.html', context)


def insert(r):
    ########1
    frm = Traineeform()
    context = {}
    context['form'] = frm
    if (r.method == 'GET'):
        return render(r, 'insert.html', context)
    else:
        frm = Traineeform(r.POST)
        if (frm.is_valid()):
            t = Trainee()
            t.name = r.POST['name']
            t.nid = r.POST['nid']
            Course = r.POST['courses']
            t.save()
        return redirect('/Trainee/list')
    ########2
    # context = {}
    # courses = Course.objects.all()
    # context['courses'] = courses
    # context['id'] = 1
    # if (r.method == 'GET'):
    #     return render(r, 'insert.html', context)
    # else:
    #     print(r.POST)
    #     Trainee.objects.create(name=r.POST['name'], courses=Course.objects.get(id=r.POST['course']),
    #                            nid=r.POST['nid'])
    #     # r.save()
    #     return render(r, 'insert.html', context)


####3
# context = {}
# context['id'] = 1
# context['form'] = Traineeform()
# Trainees = Traineeform()
#
# if (r.method == 'GET'):
#     return render(r, 'insert.html')
# else:
#     # Trainee.objects.create(name=r.POST['name'],nid=r.POST['nid'],courses=r.POST['courses'])
#     t=Trainee()
#     t.name=r.POST('name')
#     t.nid = r.POST('nid')
#     t.courses = r.POST('cousres')
#     t.save()
#     return render(r, "insert.html", {'form': Trainees},context)

class DeleteView(View):
    def get(self, request, id):
        trainees = get_object_or_404(Trainee, pk=id)
        trainees.delete()
        print(trainees)
        return redirect('/Trainee/list')

    def post(req, request, id):
        return redirect('/Trainee/list')


# class DeleteView(View):
#     def get(self, request):
#         trainees = Trainee.objects.all()
#         for trainee in trainees:
#             print(trainee.id, trainee.name, trainee.courses)
#         context = {}
#         context['title'] = 'List'
#         context['trainees'] = trainees
#         return render(request, 'list.html', context)
#     def post(req,request, id):
#         trainees = get_object_or_404(Trainee, pk=id)
#         trainees.delete()
#         print(trainees)
#         return redirect('/Trainee/list')


# def updates(request, id):
#     trainees = get_object_or_404(Trainee, pk=id)
#     courses = Course.objects.all()
#     if request.POST:
#         c = Course.objects.get(id=request.POST["course"])
#         # trainees.objects.save(
#         #     name=request.POST["trainees_name"],
#         #     nid=request.POST["trainees_nid"],
#         #     courses=c
#         # )
#         trainees.name = request.POST["name"]
#         trainees.nid = request.POST["nid"]
#         trainees.courses = c
#         trainees.save()
#
#         return redirect("/Trainee/list")
#         # return HttpResponse("sss")
#
#     return render(request, "update_form.html", context={"trainees": trainees, "courses": courses})
#
#     # return HttpResponse(trainees)


class TraineeUpdateView(UpdateView):
    model = Trainee
    fields = '__all__'
    def get(self,request,id):
        trainees = get_object_or_404(Trainee, pk=id)
        print(trainees)
        courses = Course.objects.all()
        if request.POST:
            c = Course.objects.get(id=request.POST["course"])
            trainees.name = request.POST["name"]
            trainees.nid = request.POST["nid"]
            trainees.courses = c
            trainees.save()
            print(trainees)
            return HttpResponse('save')
        return render(request, "update_form.html", context={"trainees": trainees, "courses": courses})
    def post(req, request,id):
        trainees = get_object_or_404(Trainee, pk=id)
        c = Course.objects.get(id=request.POST["course"])
        trainees.name = request.POST["name"]
        trainees.nid = request.POST["nid"]
        trainees.courses = c
        trainees.save()
        return redirect("/Trainee/list")