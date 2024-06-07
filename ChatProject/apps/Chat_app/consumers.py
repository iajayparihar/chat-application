from channels.consumer import SyncConsumer, AsyncConsumer, StopConsumer

class MyConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('WebSocket is connected...', event)
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print('Message received from client')
        print(event['text'])

        self.send({
            'type': 'websocket.send',
            'text': 'Message sent to client from server',
        })

    def websocket_disconnect(self, event):
        print('WebSocket is disconnected...', event)
        raise StopConsumer()
