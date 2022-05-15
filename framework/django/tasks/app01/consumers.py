from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from app01 import models
import json

CONN_LIST = []


class AuditConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # print("有人来链接了")
        self.accept()

        task_id = self.scope['url_route']['kwargs'].get("tid")
        # async_to_sync(self.channel_layer.group_add)(group, self.channel_name)
        node_data_array = []
        data_list = models.AuditTask.objects.filter(task_id=task_id).order_by("-id")
        mapping = {item.parent_id: item.id for item in data_list}

        for item in data_list:
            color = models.AuditTask.status_mapping[item.status]
            info = {'key': item.id, 'text': item.user, 'color': color}
            pid = mapping.get(item.id)
            if pid:
                info['parent'] = pid

            node_data_array.append(info)
        context = {
            'msg_type': 1,
            'node_data_array': node_data_array
        }
        self.send(json.dumps(context, ensure_ascii=False))

    def websocket_receive(self, message):
        text = message['text']
        print("接收到消息了 -->", text)
        task_id = self.scope['url_route']['kwargs'].get("tid")
        text_dict = json.loads(text)
        user = text_dict["user"]
        content = text_dict["type"]
        if content == "同意":
            audit_object = models.AuditTask.objects.filter(task_id=task_id, user=user).first()
            audit_object.status = 3
            audit_object.save()

            info = {
                'color': models.AuditTask.status_mapping[audit_object.status],
                "key": audit_object.id,
                'msg_type': 2}
            self.send(json.dumps(info))
            if audit_object.parent:
                audit_object.parent.status = 2
                audit_object.parent.save()
                info = {
                    'color': models.AuditTask.status_mapping[audit_object.parent.status],
                    "key": audit_object.parent.id,
                    'msg_type': 2}
                self.send(json.dumps(info))
        else:
            audit_object = models.AuditTask.objects.filter(task_id=task_id, user=user).first()
            audit_object.status = 4
            audit_object.save()

            info = {
                'color': models.AuditTask.status_mapping[audit_object.status],
                "key": audit_object.id,
                'msg_type': 2}
            self.send(json.dumps(info))

    # res = "{} SB".format(text)
    # if text == "close":
    #     self.close()
    #     raise StopConsumer
    #     return
    # for conn in CONN_LIST:
    #     conn.send(res)
    # group = self.scope['url_route']['kwargs'].get("group")
    # async_to_sync(self.channel_layer.group_send)(group, {"type": "xx.oo", 'message': message})

    def xx_oo(self, event):
        text = event['message']['text']
        self.send(text)

    def websocket_disconnect(self, message):
        print("客户端主动断开链接")
        # CONN_LIST.remove(self)
        # group = self.scope['url_route']['kwargs'].get("group")
        # async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
        raise StopConsumer
