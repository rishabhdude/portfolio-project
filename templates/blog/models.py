from django.db import models

# Create a Blog models
#What sort of properties to look for here

class Blog(models.Model):
     title=models.CharField(max_length=225)
     pub_date = models.DateTimeField()
     body = models.TextField()
     image=models.ImageField(upload_to='images/')

     def summary(self):
         return self.body[:100]

     def pub_date_clean(self):
         return self.pub_date.strftime('%b %e %Y')
