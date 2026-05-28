from django.contrib import admin
from .models import Question, Choice, Submission

# Choice Inline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text',)

# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id',)

# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)