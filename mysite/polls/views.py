from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from . models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    """
    Handle the detail view for a specific question.

    This view attempts to retrieve a `Question` object from the database
    using the provided `question_id`. If the `Question` does not exist,
    it raises an `Http404` exception. If the `Question` is found, it renders
    the "polls/detail.html" template with the `question` object passed as context.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question to retrieve.

    Returns:
        HttpResponse: The rendered detail page for the question.

    Raises:
        Http404: If the `Question` with the given `question_id` does not exist.

    Note:
        - `pk` stands for "primary key", which is a unique identifier for a record in the database.
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #   Or simply just
    #   question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)