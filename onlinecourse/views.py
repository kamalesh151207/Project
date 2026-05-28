from django.shortcuts import render
from .models import Course, Question, Choice, Submission

def exam(request):
    course = Course.objects.first()
    questions = Question.objects.filter(course=course)
    return render(request, "exam.html", {"questions": questions})


def submit(request):
    if request.method == "POST":
        score = 0
        total = 0

        questions = Question.objects.all()

        for q in questions:
            total += 1
            selected = request.POST.get(str(q.id))

            if selected:
                choice = Choice.objects.get(id=selected)
                if choice.is_correct:
                    score += 1

        submission = Submission.objects.create(
            user="student",
            score=score,
            total=total
        )

        return render(request, "result.html", {
            "score": score,
            "total": total
        })


def show_exam_result(request):
    result = Submission.objects.last()
    return render(request, "result.html", {"result": result})