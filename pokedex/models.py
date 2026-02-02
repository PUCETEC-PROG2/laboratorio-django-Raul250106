from django.db import models

# Create your models here.
class Trainer (models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    level = models.IntegerField()
    birth = models.DateField()
    picture = models.ImageField(upload_to='trainer_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Pokemon (models.Model):
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    picture = models.ImageField(upload_to='pokemon_pictures/', null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete= models.SET_NULL, null= True)

    def __str__(self):
        return self.name