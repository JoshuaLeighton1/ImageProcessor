from django.db import models
from django.core.validators import validate_image_file_extension

# Create your models here.

#imageField model with validators
class ImageField(models.Model):
    uploaded_image_file = models.ImageField(upload_to="images/", validators=[validate_image_file_extension])
    avg_hex_value = models.CharField(max_length=50)
    rgb_val = models.CharField(max_length=50)
    color_name = models.CharField(max_length=50)



