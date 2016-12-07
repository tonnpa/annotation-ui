from django.http import HttpResponse
from django.shortcuts import render

from .models import Drug, Annotation, Person


def index(request):
    context = {
        'annotators': Person.objects.all()
    }
    return render(request, 'welcome.html', context)


def annotate(request, person_id):
    annotator = Person.objects.get(id=person_id)
    drugs = Drug.objects.filter(annotator=person_id)
    if not drugs.exists():
        message = "Good job {}, no more drugs left to be annotated!".format(annotator.first_name)
        return render(request, 'message.html', {'message': message})

    context = {
        'drug': drugs.first(),
        'annotations': Annotation.objects.filter(key=drugs.first().key),
        'options': Annotation.ANNOTATION,
    }
    return render(request, 'index.html', context)


def partial_drug_detail(request, drug_id):
    context = {
        'drug': Drug.objects.get(key=drug_id),
    }
    return render(request, 'partials/drugdetail.html', context)


def partial_annotations(request, drug_id):
    context = {
        'options': Annotation.ANNOTATION,
        'annotations': Annotation.objects.filter(key=drug_id)
    }
    return render(request, 'partials/annotations.html', context)
