from django.db import models

class SearchLog(models.Model):
    session_id = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    user_ip = models.CharField(max_length=100)
    user_agent = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    device = models.CharField(max_length=50, default="unknown")
    browser = models.CharField(max_length=50, default="unknown")
    os = models.CharField(max_length=50, default="unknown")
    city = models.CharField(max_length=100, default="unknown")
    country = models.CharField(max_length=100, default="unknown")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.message[:30]} ({self.user_ip})"