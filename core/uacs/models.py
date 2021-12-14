from django.db import models


class UACSBase(models.Model):
    label = models.CharField(max_length=300)
    code = models.CharField(max_length=5)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Region(UACSBase):
    pass


class Province(UACSBase):
    parent = models.ForeignKey(Region, on_delete=models.CASCADE)


class CityMunicipality(UACSBase):
    parent = models.ForeignKey(Province, on_delete=models.CASCADE)


class Barangay(UACSBase):
    parent = models.ForeignKey(CityMunicipality, on_delete=models.CASCADE)
