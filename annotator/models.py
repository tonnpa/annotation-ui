from django.db import models


# Create your models here.


class Drug(models.Model):
    key = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    overview = models.TextField()
    cl_phase_1 = models.CharField(max_length=256)
    cl_phase_2 = models.CharField(max_length=256)
    cl_phase_3 = models.CharField(max_length=256)

    def __str__(self):
        return str(self.key) + ' | ' + self.name


class Annotation(models.Model):
    key = models.ForeignKey(Drug)

    I_PLUS = 'i+'
    I_MINUS = 'i-'
    I_ZERO = 'i0'
    S_PLUS = 's+'
    S_MINUS = 's-'
    S_ZERO = 's0'
    O = 'o'
    ANNOTATION = (
        (I_PLUS, 'i+'),
        (I_MINUS, 'i-'),
        (I_ZERO, 'i0'),
        (S_PLUS, 's+'),
        (S_MINUS, 's-'),
        (S_ZERO, 's0'),
        (O, 'o')
    )

    annotation = models.CharField(
        max_length=2,
        choices=ANNOTATION,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.key.key) + ' | ' + self.key.name + ' | ' + self.annotation
