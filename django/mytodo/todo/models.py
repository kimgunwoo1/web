from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # table 상에 빈 값으로 들어 갈 수 있다.
    create = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    #완료 여부, 중요한 일 여부

    def __str__(self):
        return self.title