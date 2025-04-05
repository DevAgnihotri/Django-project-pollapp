from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
    # This function checks if the publication date (`pub_date`) of an object
    # is within the last 24 hours (1 day) from the current time.

    # `timezone.now()` retrieves the current date and time, considering timezone settings.
    # `datetime.timedelta(days=1)` represents a time duration of 1 day.
    # Subtracting this timedelta from the current time gives the time exactly 24 hours ago.

    # The comparison `self.pub_date >= timezone.now() - datetime.timedelta(days=1)`
    # checks if the publication date (`pub_date`) is greater than or equal to
    # the time 24 hours ago. If true, it means the object was published recently.
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
