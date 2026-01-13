from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    color = models.CharField(max_length=7, default='#007aff')
    is_all_day = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True) 
    time = models.TimeField(null=True, blank=True)
    color = models.CharField(max_length=7, default='#007aff')

    class Meta:
        # '-' を削除して、作成日時が古い順（追加した順）に並ぶようにします
        ordering = ['created_at']

    def __str__(self):
        return self.title