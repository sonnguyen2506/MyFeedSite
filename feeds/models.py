from django.db import models

from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.cat_name

class Feed(models.Model):
    Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL) #models.CASCADE
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=250)
    guid = models.IntegerField(default=0)
    pubDate = models.CharField(max_length=100)

    def __str__(self):
        return self.title
