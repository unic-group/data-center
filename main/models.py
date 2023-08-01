from django.db import models

# Create your models here.

class Weather(models.Model):
    city = models.CharField(verbose_name="Viloyat nomi: " , max_length=150)
    lat = models.CharField(verbose_name="Viloyat kengligi: " , max_length=150)
    lon = models.CharField(verbose_name="Viloyat uzunligi: " , max_length=150)
    image = models.ImageField(verbose_name="Viloyat rasmi: " , upload_to="image_test")
    reg_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.city
    class Meta:
        verbose_name = "Ob-havo"
        verbose_name_plural = "Ob-havo"