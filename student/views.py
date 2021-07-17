from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import StudentDetail
# Create your views here.
from .forms import CreateStudent
from django.contrib import messages
from django.views.generic import UpdateView
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url="signin")
def studentRegistrations(request):
    form = CreateStudent(request.POST, request.FILES)
    if request.method == "POST":
        # import pdb;pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "Student registration successful")
            return redirect('student_list')
    else:
        form = CreateStudent()
    return render(request, 'student/registration.html', {'form': form})


@login_required(login_url="signin")
def studentList(request):
    student_data = StudentDetail.objects.all().order_by('-id')
    paginator = Paginator(student_data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # import pdb;pdb.set_trace();
    if "search" in request.GET:
        # import pdb;pdb.set_trace()
        searched_text = request.GET['search']
        if searched_text == "":
            return render(request, 'student/student_list.html', {'data': student_data, 'page_obj': page_obj})
        elif StudentDetail.objects.filter(
                Q(name__icontains=searched_text) | Q(student_id=searched_text)).exists() == False:
            return render(request, 'student/student_list.html', {'data_not_found': "data not found"})

        else:
            searched_data = StudentDetail.objects.filter(Q(name__icontains=searched_text) | Q(student_id=searched_text))
        return render(request, 'student/student_list.html', {'page_obj': searched_data})

    return render(request, 'student/student_list.html', {'data': student_data, 'page_obj': page_obj})


def studentUpdate(request, id):
    student_edit = StudentDetail.objects.get(id=id)
    # import pdb;pdb.set_trace()
    edit_form = CreateStudent(instance=student_edit)

    if request.method == "POST":
        edit_form = CreateStudent(request.POST or None, request.FILES or None, instance=student_edit)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, "student update successfully")
            return redirect('student_list')

    return render(request, 'student/student_update.html', {'data': edit_form})


def deleteStudent(request, id):
    deleted_obj = StudentDetail.objects.get(id=id)
    deleted_obj.delete()
    return redirect('student_list')

