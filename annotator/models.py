from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Drug(models.Model):
    key = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    overview = models.TextField()
    cl_phase_1 = models.CharField(max_length=256)
    cl_phase_2 = models.CharField(max_length=256)
    cl_phase_3 = models.CharField(max_length=256)
    annotator = models.ForeignKey(Person)

    def __str__(self):
        return str(self.key) + ' | ' + self.name


class Annotation(models.Model):
    key = models.ForeignKey(Drug)
    cui = models.CharField(max_length=16, null=True, blank=True)
    mdr1 = models.CharField(max_length=256, null=True, blank=True)

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

    class Meta:
        unique_together = ('key', 'cui')

    def __str__(self):
        return str(self.key.key) + ' | ' + self.key.name + ' | ' + self.cui + ' | ' + str(self.annotation)
