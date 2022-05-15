import os
import sys
import django
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tasks.settings")
django.setup()

from app01 import models

node_data_array = []
data_list = models.AuditTask.objects.filter(task_id=2).order_by("-id")
mapping = {item.parent_id: item.id for item in data_list}


for item in data_list:
    color = models.AuditTask.status_mapping[item.status]
    info = {'key': item.id, 'text': item.user,  'parent':mapping.get(item.id),'color':color}
    node_data_array.append(info)
print(json.dumps(node_data_array, indent=2, ensure_ascii=False))
