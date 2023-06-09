from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, 
                            verbose_name='название населённого пункта',
                            unique=True)
    slug =models.CharField(max_length=50, blank=True, unique=True)
                            
    
    class Meta:
        verbose_name = 'Название населённого пункта'
        verbose_name_plural = 'Название населённых пунктов'
        
    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=50, 
                            verbose_name='Язык пограммирования',
                            unique=True)
    slug =models.CharField(max_length=50, blank=True, unique=True)
                            
    
    class Meta:
        verbose_name = 'Язык пограммирования'
        verbose_name_plural = 'Языки пограммирования'
        
    def __str__(self):
        return self.name