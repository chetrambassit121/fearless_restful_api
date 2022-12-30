from django.db import models


"""
Creating an Item Model
"""
class Item(models.Model):
    
    """
    Creating fields to define Item Model
    """
    name = models.CharField(max_length=100, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)

    """
    Inner class, defaulting all Item objects (models) to display in descending order
    """
    class Meta:
        ordering = ['created']

    """
    Defining save method, saving all arguments and keyword arguments
    """
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
