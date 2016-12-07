from django.contrib import admin
from .models import Annotation, Drug, Person

admin.site.register(Annotation)
admin.site.register(Drug)
admin.site.register(Person)
