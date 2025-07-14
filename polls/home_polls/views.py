from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from .models import Question, Choice

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_questions': latest_questions,
    }
    return render(request, 'home_polls/index.html', context)

def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    
    return render(request, 'home_polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'home_polls/results.html', {'question': question})

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form with error message
            messages.error(request, 'You didn\'t select a choice.')
            return render(request, 'home_polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            messages.success(request, f'Your vote for "{selected_choice.choice_text}" has been recorded!')
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data to prevent data from being posted twice if user
            # hits the Back button.
            return redirect('home_polls:results', question_id=question.id)
    
    # If not POST request, redirect to detail page
    return redirect('home_polls:detail', question_id=question.id)

