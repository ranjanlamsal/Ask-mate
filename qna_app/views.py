from django.shortcuts import render, redirect
from .models import QuestionModel, AnswerModel, CategoryModel
from .forms import QuestionForm, AnswerForm # importing form to display
from django.http import HttpResponse
from django.views.generic import CreateView, ListView


def question(request):
    Question = QuestionModel.objects.all()
    return render(request,'question.html',{'question':Question})

def list_question(request):
    Question = QuestionModel.objects.all()
    return render(request, 'qna_app/list.html', {'question': Question})


def add_question(request):

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('qna:read')

        else:
            print(form.errors)
            return HttpResponse('Invalid Form')


    else:

        #form = QuestionForm
        category= CategoryModel.objects.all()
        return render(request, 'qna_app/create.html', {'category': category})


def update_question(request, id):
    ques = QuestionModel.objects.get(id=id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=ques)

        if form.is_valid():
            form.save()
            return redirect('qna:list')

        else:
            return HttpResponse('Invalid Form')

    else:
        form = QuestionForm(instance=ques)
        return render(request, 'qna_app/update.html/', {'form': form})


def delete_question(request, id):
    ques = QuestionModel.objects.get(id=id)
    ques.delete()
    return redirect('qna:list')


def vote_question(request, id):
    instance = QuestionModel.objects.get(id=id)
    vote = instance.question_votes +1
    instance.question_votes = vote
    instance.save()
    return redirect('qna:read')

def answer(request,id):
    if request.method == "POST":
        by= request.POST.get('answered_by')
        desc = request.POST.get('answer_desc')
        answer_img = request.POST.get('answer_img')
        question = QuestionModel.objects.get(id=id)
        Comment = AnswerModel(answered_by=by, answer_desc=desc, answer_img=answer_img,
        question=question)
        Comment.save()
        return HttpResponse('SUCCESS')
    else:
        form= AnswerForm
        a={'form':form}
        b={'id':id}
        c={**a,**b}
        return render(request,'ans_create.html')


class QuestionListView(ListView):
    queryset = QuestionModel.objects.all()