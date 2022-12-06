from django.db import models

class Department(models.Model):
    class Meta:
        db_table = 'hr-department'
        verbose_name_plural = 'Hr Department'
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name