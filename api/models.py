from django.db import models
import json


# Create your models here.


class Information(models.Model):
    country = models.CharField(max_length=250)
    flag = models.URLField(editable=False)
    country_code = models.CharField(max_length=250, editable=False)
    csirt = models.CharField(max_length=250, default='None', null=True, blank=True)
    web = models.URLField(default='None', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        with open('country.json', 'r') as file:
            data_list = json.load(file)

        for data in data_list:
            user_country = self.country.lower()
            data_country = data['country'].lower()
            if user_country == data_country:
                self.flag = data['flag']
                self.country_code = data['code']
                break
        else:
            raise ValueError('Please enter a valid country')

        super(Information, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Information'

    def __str__(self):
        return self.country
