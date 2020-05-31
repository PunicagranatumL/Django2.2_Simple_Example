from django.db import models

# Create your models here.

class TodoItem(models.Model):
    todo_item = models.CharField(max_length=50,verbose_name="事件")
    todo_date = models.DateTimeField(auto_now_add=True,verbose_name="时间")

    class Meta:
        verbose_name = "简单的记事本"
        verbose_name_plural = "简单的记事本"
        ordering = ["-todo_date"]
