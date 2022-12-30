from django.db import models



class Item(models.Model):
    """
    Creating an Item Model
    """
   
    name = models.CharField(max_length=100, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    """
    Creating fields to define Item Model
    """

   
    class Meta:
        """
        Inner class, defaulting all Item objects (models) to display in descending order
        """
        ordering = ['created']

    
    def save(self, *args, **kwargs):
        """
        Defining save method, saving all arguments and keyword arguments
        """
        super().save(*args, **kwargs)
