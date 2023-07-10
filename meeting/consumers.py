import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):

        self.meeting_id = self.scope["url_route"]["kwargs"]["meetingId"]
        self.meeting_room = "meeting_room_%s" % self.meeting_id

        async_to_sync(self.channel_layer.group_add)(
            self.meeting_room, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.meeting_room, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        async_to_sync(self.channel_layer.group_send)(self.meeting_room, {"type": "reload"})

    def reload(self, event):
        self.send(text_data=json.dumps({"message": "reload"}))