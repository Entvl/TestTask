import uuid

from django.db import models
from django.utils.timezone import now

class Course(models.Model):
    name = models.CharField("Name", max_length=120)
    icon = models.ImageField("Icon", upload_to="icons/", default="default-image-620x600.jpg")
    description = models.TextField("Description", default="")
    price = models.IntegerField("Price", default=0)
    start_date = models.DateField("Start date", default=now)
    end_date = models.DateField("End date", default=now)
    user = models.CharField("User id", default="1", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"