from django.db import models

from django.contrib.auth.models import User

class Code(models.Model): 
    """codes for access system"""
    code_input = models.CharField(max_length=1, null=True, blank=True, default="k")
    code_number = models.CharField(max_length=15, null=True, blank=True, default="")
    pin = models.CharField(max_length=6, null=True, blank=True, default=None, unique=False)
    code_type = models.CharField(max_length=3, null=True, blank=True, default="")
    valid_from = models.DateTimeField(null=True, blank=True, default=None)
    valid_to = models.DateTimeField(null=True, blank=True, default=None)
    created = models.DateTimeField(null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    comment = models.CharField(max_length=200, null=True, blank=True, default=None)

    class Meta: 
        unique_together = ("code_input", "code_number")


    def save(self, *args, **kwargs): 
        self.code_input = self.code_input.lower()
        self.code_number = self.code_number.lower()
        super(Code, self).save(*args, **kwargs)



class Event(models.Model): 
    """events for access system"""
    event_type = models.CharField(max_length=10, null=True, blank=True, default = None) 
    short_description = models.CharField(max_length=10, unique=True) 
    long_description = models.CharField(max_length=200, null=True, blank=True, default = None) 
    event_begin = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)

    
