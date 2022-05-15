import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tasks.settings")
django.setup()

from app01 import models

task_object = models.Task.objects.create(title="请30天假期", detail="no mood")
user_order = ["村长", "乡长", "县长", "市长"]
node = None
for i in range(len(user_order) - 1, -1, -1):
    current_user = user_order[i]
    node = models.AuditTask.objects.create(
        task=task_object,
        status= 2 if i == 0 else 1,
        user=current_user,
        parent=node
    )
