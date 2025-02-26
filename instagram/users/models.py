from django.db import models


class Victim(models.Model):

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Victim'
        verbose_name_plural = 'Victims'
        ordering = ['username']
        db_table = 'victims'

    def __str__(self):
        return self.username