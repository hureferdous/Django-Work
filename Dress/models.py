from django.db import models

class Cloth(models.Model):
    dress_size = models.CharField(max_length=200)
    dress_color = models.CharField(max_length=200)
    dress_price = models.CharField(max_length=200)
    dress_title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=20)

    def __str__(self):
        return self.dress_title + ' - ' + self.file_type

class Brand(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=200)


