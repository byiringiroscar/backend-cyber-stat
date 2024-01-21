from django.db import models
import json
import os
import uuid
import uuid as uuid_lib


# Create your models here.


class Information(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    country = models.CharField(max_length=250)
    flag = models.URLField()
    country_code = models.CharField(max_length=250)
    csirt = models.CharField(max_length=250, default='None', null=True, blank=True)
    web = models.URLField(default='None', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'country.json')
        with open(file_path, 'r') as file:
            data_list = json.load(file)
        user_country = self.country.lower()
        for data in data_list:
            data_country = data['country'].lower()
            if user_country == data_country:
                self.flag = data['flag']
                self.country_code = data['code']
                break

        super(Information, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Information'

    def __str__(self):
        return self.country
