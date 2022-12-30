from django.db import models


"""
Using class to create an Item object 
"""
class Item(models.Model):
    
    """
    Creating fields to define Item object
    """
    name = models.CharField(max_length=100, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)

    """
    Inner class, defaulting all Item objects to display in descending order
    """
    class Meta:
        ordering = ['created']

    """
    Defining save method, saving all arguements and keyword arguements
    """
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
