from rest_framework.viewsets import ModelViewSet
from annotator.models import Drug, Annotation
from annotator.serializers import DrugSerializer, AnnotationSerializer


class DrugViewSet(ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class =  DrugSerializer


class AnnotationViewSet(ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
