from django.db import models

class EnergyData(models.Model):
    end_year = models.CharField(max_length=4, blank=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=255, blank=True , null=True)
    topic = models.CharField(max_length=255 , blank=True , null=True)
    insight = models.CharField(max_length=255, blank=True , null=True)
    url = models.URLField(blank=True , null=True)
    region = models.CharField(max_length=255 , blank=True , null=True)
    start_year = models.CharField(max_length=4, blank=True , null=True)
    impact = models.CharField(max_length=255, blank=True , null=True)
    
    added = models.DateTimeField(auto_now_add=False , auto_now= False , blank=True , null=True )
    published = models.DateTimeField(auto_now_add=False , auto_now= False  ,blank=True , null=True)
    
    country = models.CharField(max_length=255,blank=True , null=True)
    relevance = models.IntegerField(blank=True , null=True)
    pestle = models.CharField(max_length=255 , blank=True , null=True)
    source = models.CharField(max_length=255, blank=True , null=True)
    title = models.CharField(max_length=255, blank=True , null=True)
    likelihood = models.IntegerField()

    def __str__(self):
            return self.title
