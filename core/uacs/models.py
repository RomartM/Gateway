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


class Address(models.Model):
    in_ph = models.BooleanField(default=True, help_text='In philippines')
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(CityMunicipality, on_delete=models.DO_NOTHING)
    barangay = models.ForeignKey(Barangay, on_delete=models.DO_NOTHING)
    zip = models.CharField(max_length=80, default='')
    street = models.TextField()
    fallback_address = models.TextField(blank=True)
