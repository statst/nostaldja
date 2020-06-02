from django.db import models

# Create your models here.

#Define a class for Decades
#primary key
class Decade(models.Model):
    start_year=models.CharField(max_length=12)

    def __str__(self):
        return self.start_year


# Define a class for Fad that inherits from the mode.Model class
#name = CharField(max_length =100)
# image_url=UrlField()
# description=TextField()
# decade= foreign key

class Fad(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.name
#Don't forget when don to make migrations and migrate
