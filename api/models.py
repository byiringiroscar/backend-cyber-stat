from django.db import models

# Create your models here.


class Information(models.Model):
    country = models.CharField(max_length=250)
    flag = models.URLField()
    csirt = models.CharField(max_length=250, default='None', null=True, blank=True)
    web = models.URLField(default='None', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Information'

    def __str__(self):
        return self.country
