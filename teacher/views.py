from django.shortcuts import render, redirect
from .models import TeacherDetail
from .forms import TeacherDetailForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="signin")
def teacherRegisteration(request):
    form = TeacherDetailForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "teacher registration successful")
            return redirect('teacher_list')
    else:
        form = TeacherDetailForm()

    return render(request, 'teacher/teacher_registration.html', {'form': form})


@login_required(login_url="signin")
def teacherList(request):
    pegi_data = TeacherDetail.objects.all().order_by('-id')
    paginator = Paginator(pegi_data, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'search' in request.GET:
        user_searched_text = request.GET['search']
        if user_searched_text == "":
            return render(request, 'teacher/teacher_list.html', {'page_obj': page_obj})
        elif TeacherDetail.objects.filter(
                Q(name__icontains=user_searched_text) | Q(teacher_id=user_searched_text)).exists() == False:
            return render(request, 'teacher/teacher_list.html', {'data_not_found': "data not found"})

        else:
            searched_objects = TeacherDetail.objects.filter(
                Q(name__icontains=user_searched_text) | Q(teacher_id=user_searched_text))
            return render(request, 'teacher/teacher_list.html', {'page_obj': searched_objects})
    return render(request, 'teacher/teacher_list.html', {'page_obj': page_obj})


def teacherUpdate(request, id):
    object = TeacherDetail.objects.get(id=id)
    edit_form = TeacherDetailForm(request.POST, request.FILES, instance=object)

    if request.method == "POST":
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, "Teacher update successful")
            return redirect("teacher_list")
    else:
        edit_form = TeacherDetailForm(instance=object)

    return render(request, 'teacher/teacher_update.html', {'data': edit_form})


def deleteTeacher(request, id):
    deleted_obj = TeacherDetail.objects.get(id=id)
    deleted_obj.delete()
    return redirect("teacher_list")
