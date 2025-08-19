from django.db import models

class DiseaseScan(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='disease_scans/')
    result_label = models.CharField(max_length=100, blank=True, default='')
    confidence = models.FloatField(default=0.0)

    def __str__(self):
        return f"Scan {self.id} - {self.result_label}"
