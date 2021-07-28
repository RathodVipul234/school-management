from django.shortcuts import render, redirect
from .models import TeacherDetail, Test
from .forms import TeacherDetailForm, TestForm, test_formset, test_formset_txt
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


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


def create_test(request):
    form1 = test_formset(request.POST, request.FILES)
    form_txt = test_formset_txt(request.POST)
    teacher = TeacherDetail.objects.all()
    if request.method == 'POST':
        teacher_name = request.POST['teacher_name']
        teacher_instance = TeacherDetail.objects.get(name=teacher_name)
        question_id = request.POST['question_id']
        if len(form1.cleaned_data) or len(form_txt.cleaned_data) == 0:
            messages.error(request, "minimum 1 files and 1 text field required")
            return redirect('test')

        if form1.is_valid():
            for i in form1:
                data = i.cleaned_data.items()
                if len(data) == 0:
                    break
                Test.objects.create(
                    questions_id=question_id,
                    teacher=teacher_instance,
                    questions=i.cleaned_data['questions']
                )

        if form_txt.is_valid():
            for j in form_txt:
                data = j.cleaned_data.items()
                if len(data) == 0:
                    break
                Test.objects.create(
                    questions_id=question_id,
                    teacher=teacher_instance,
                    questions_txt=j.cleaned_data['questions_txt']
                )

        messages.success(request, "test upload successfully")
        return redirect('home')
    else:
        form1 = test_formset()
        form_txt = test_formset_txt()
        # import pdb;pdb.set_trace()
        input = "text"
    return render(request, 'test/create_test.html', {'form1': form1, 'teacher': teacher, 'form_txt': form_txt}, )

def test_questions(request):
    obj = Test.objects.all().distinct('questions_id')
    return render(request, 'test/questions_list.html', {'data': obj})


def update_questions(request, id):
    obj = Test.objects.filter(questions_id=id)
    files_questions = []
    texts_questions = []

    for i in obj:
        if i.questions_txt != "":
            texts_questions.append(i)
        else:
            files_questions.append(i)

    if request.method == "POST":
        countFile = request.POST['counterFiles']
        countText = request.POST['counterText']
        for i in range(1, int(countFile) + 1):
            try:
                newFile = request.FILES['new-file-{}'.format(i)]
                instance = Test.objects.filter(questions_id=request.POST['question_id'])[i - 1]
                instance.questions = newFile
                instance.save()
            except:
                pass
        for j in range(1, int(countText) + 1):
            try:
                newText = request.POST.get('new-txt-{}'.format(j))
                instance = Test.objects.filter(questions_id=request.POST['question_id'])[j - 1]
                instance.questions_txt = newText
                instance.save()
            except:
                pass
        messages.success(request, 'questions update successfully')
        return redirect('home')
    return render(request, 'test/update_questions.html',
                  {'obj': obj, 'texts_questions': texts_questions, 'files_questions': files_questions})
