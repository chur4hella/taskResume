from django.db import models
from django.contrib.postgres.fields import JSONField


class Field(models.Model):
    data_field = JSONField()

    def __str__(self):
        return str(self.data_field)