from django.db import models


# Create your models here.


class Task(models.Model):
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="标题", null=True, blank=True)


class AuditTask(models.Model):
    task = models.ForeignKey(verbose_name="任务", to="Task", on_delete=models.CASCADE)
    status_choices = (
        (1, "未审批"),
        (2, "待审批"),
        (3, "通过"),
        (4, "未通过"),
    )
    status_mapping={
        1:"lightgrey",
        2: "lightgreen",
        3: "green",
        4: "red",
    }
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)
    user = models.CharField(verbose_name="审批者", max_length=64)
    parent = models.ForeignKey(verbose_name="上一级", to="AuditTask", null=True, blank=True, related_name="xx",
                               on_delete=models.CASCADE)
