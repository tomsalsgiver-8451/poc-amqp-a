from proton import Message
from proton.handlers import MessagingHandler


class Handler(MessagingHandler):
    # Constructor
    def __init__(self, server, address, inputModel):
        super(Handler, self).__init__()
        self.server = server
        self.address = address
        self.inputModel = inputModel

    # Called when container is created
    # Here we are establishing a connection to the broker
    # Then declaring this handler as a receiver
    def on_start(self, event):
        conn = event.container.connect(self.server)
        event.container.create_sender(conn, self.address)
        event.container.create_receiver(conn, "poc-a")

    # Called when connection to broker has been established and is ready to send a message
    # Close the connection after it is sent to the queue
    def on_sendable(self, event):
        msg = Message(body=self.inputModel.json())
        event.sender.send(msg)
        event.sender.close()

    # Called when a message is received on the poc-a queue
    # Closes the connection so that the 200 can return on the endpoint
    def on_message(self, event):
        print("Received back", event.message)
        event.connection.close()
