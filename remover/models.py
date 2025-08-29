from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100,unique = True)
    icon = models.ImageField(upload_to='icon/')
    description = models.TextField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class FeatureTask(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name="tasks")
    input_file_1 = models.FileField(upload_to="inputs/", blank=True, null=True)
    input_file_2 = models.FileField(upload_to="inputs/", blank=True, null=True)  # optional (e.g., video in "find image in video")
    output_file = models.FileField(upload_to="outputs/", blank=True, null=True)

    reated_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.feature.name} Task ({self.id})"

