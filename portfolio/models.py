from django.db import models

class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack  = models.CharField(max_length=200, help_text="Comma-separated list")
    project_url = models.URLField(blank=True)
    image_url   = models.URLField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title        = models.CharField(max_length=200)
    slug         = models.SlugField(unique=True)
    content      = models.TextField()
    published_at = models.DateTimeField()
    
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name      = models.CharField(max_length=100)
    email     = models.EmailField()
    message   = models.TextField()
    sent_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
