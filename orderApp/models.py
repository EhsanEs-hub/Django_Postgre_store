from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Customers(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null=False, blank=False,
                              validators=[validate_file_extension])
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.customer.first_name + " " + self.customer.last_name

class Products(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    cover = models.FileField(upload_to='files/products_cover/', null=False, blank=False,
                             validators=[validate_file_extension])

    def __str__(self):
        return self.title

class OrderApp(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    description = RichTextField()

    def __str__(self):
        return self.title