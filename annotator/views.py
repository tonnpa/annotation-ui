from django.shortcuts import render
from .models import Drug, Annotation


def index(request):
    context = {
        'drug': Drug.objects.get(key=16),
        'annotations': Annotation.objects.filter(key=16),
        'options': Annotation.ANNOTATION,
    }
    return render(request, 'index.html', context)
