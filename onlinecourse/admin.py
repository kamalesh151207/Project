from django.contrib import admin
from .models import Course, Question, Choice, Submission


# Inline for Choice inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Inline for Question inside Course
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'course', 'grade')
    inlines = [ChoiceInline]


# Course Admin (LessonAdmin equivalent in your project)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [QuestionInline]


# Register models
admin.site.register(Course, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)