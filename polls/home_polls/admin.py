from django.contrib import admin

# Register your models here.
admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls Admin Portal"
admin.site.index_title = "Welcome to the Polls Admin Portal"
from .models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)