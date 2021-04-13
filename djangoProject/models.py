# from django.db import models
# from django.utils import timezone
#
# class articles(models.Model):
#     STATUS_CHOICES=(
#         ('d','draft'),('p','published')
#     )
#     titel=models.CharField(max_length=60)
#     slug=models.SlugField(max_length=60)
#     describtion=models.TextField(max_length=60)
#     tumbnail=models.ImageField(upload_to="image")
#     publish=models.TimeField(default=timezone.now)
#     created=models.TimeField(auto_now_add=True)
#     updated=models.TimeField(auto_now=True)
#     status=models.CharField(max_length=1,choices=STATUS_CHOICES)
#     def __str__(self):
#         return self.titel