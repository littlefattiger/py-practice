from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

CONN_LIST = []


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # print("有人来链接了")
        self.accept()
        # CONN_LIST.append(self)
        # self.send("来了啊 欢迎")
        group = self.scope['url_route']['kwargs'].get("group")
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)

    def websocket_receive(self, message):
        text = message['text']
        print("接收到消息了 -->", text)
        # res = "{} SB".format(text)
        # if text == "close":
        #     self.close()
        #     raise StopConsumer
        #     return
        # for conn in CONN_LIST:
        #     conn.send(res)
        group = self.scope['url_route']['kwargs'].get("group")
        async_to_sync(self.channel_layer.group_send)(group, {"type": "xx.oo", 'message': message})

    def xx_oo(self, event):
        text = event['message']['text']
        self.send(text)

    def websocket_disconnect(self, message):
        # print("客户端主动断开链接")
        # CONN_LIST.remove(self)
        group = self.scope['url_route']['kwargs'].get("group")
        async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
        raise StopConsumer
