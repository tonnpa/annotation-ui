from rest_framework.serializers import ModelSerializer
from annotator.models import Drug, Annotation


class DrugSerializer(ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class AnnotationSerializer(ModelSerializer):
    class Meta:
        model = Annotation
        fields = '__all__'
