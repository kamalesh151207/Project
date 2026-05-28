from django.contrib import admin
from .models import Course, Question, Choice, Submission

# Inline for Choices inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for Questions inside Course
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Course Admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)