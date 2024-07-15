from django.shortcuts import render, get_object_or_404
from .models import Quiz
from django.shortcuts import render, redirect
from .forms import QuizForm
from django.urls import reverse
from django.http import HttpResponseRedirect

  
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    context = {
        'quiz': quiz,
    }
    return render(request, 'quiz.html', context)

def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    selected_option = request.POST.get('option')
    correct_option = quiz.correct_option

    # Check if selected option is correct
    if selected_option == correct_option:
        is_correct = True
    else:
        is_correct = False

    context = {
        'quiz': quiz,
        'selected_option': selected_option,
        'is_correct': is_correct,
        'correct_option': correct_option,
    }
    return render(request, 'result.html', context)


 
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()  
            return redirect('quiz_list')  
    else:
        form = QuizForm()
    
    return render(request, 'quiz_form.html', {'form': form})
      