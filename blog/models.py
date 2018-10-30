from django.db import models
# Create a Blog models
# What sort of prperties to look for here
# title
# publication DjangoTemplates
# body of the Blog
# blog images

class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image=models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def pub_date_clean(self):
        return self.pub_date.strftime('%b %e %Y')




# Add the blog app to the settings
# Create a migration
#Migrate
# Add to the admin
