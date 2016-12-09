import csv
from datetime import date

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Drug, Annotation, Person

@csrf_protect
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
        'annotator': person_id,
        'drug': drugs.first(),
        'annotations': Annotation.objects.filter(key=drugs.first().key),
        'options': Annotation.ANNOTATION,
    }
    return render(request, 'index.html', context)


def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="annotations_{}.csv"'.format(date.today())
    writer = csv.writer(response)
    writer.writerow(['Drug Key', 'CUI', 'MDR1', 'Annotation'])

    for annotation in Annotation.objects.all():
        writer.writerow([annotation.key, annotation.cui, annotation.mdr1, annotation.annotation])
    return response


def get_next_drug(request, person_id):
    next_drug = Drug.objects.filter(annotator=person_id) \
        .filter(annotation__annotation__isnull='True').distinct().first()
    if next_drug is not None:
        return JsonResponse(next_drug.key, safe=False)
    return JsonResponse(None, safe=False)


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
