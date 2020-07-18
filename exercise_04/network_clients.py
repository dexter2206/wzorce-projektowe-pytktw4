from typing import Protocol, Iterable


class Client(Protocol):

    def connect(self, address, port):
        pass

    def send(self, message: str):
        pass

    def disconnect(self):
        pass


class MessageSender:

    def __init__(self, client: Client):
        self.client = client

    def send_messages(self, address, port, messages: Iterable[str]):
        self.client.connect(address, port)
        for message in messages:
            self.client.send(message)
        self.client.disconnect()


class TCPClient:

    def open_connection(self, host):
        pass

    def write(self, data: bytes):
        pass

    def close_connection(self):
        pass


class TCPClientAdapter:

    def __init__(self, tcp_client: TCPClient):
        self.tcp_client = tcp_client

    def connect(self, address, port):
        host = f"{address}:{port}"
        self.tcp_client.open_connection(host)

    def send(self, message: str):
        self.tcp_client.write(data=message.encode("utf-8"))

    def disconnect(self):
        self.tcp_client.close_connection()


if __name__ == '__main__':
    tcp_client = TCPClient()
    adapter = TCPClientAdapter(tcp_client)
    sender = MessageSender(adapter)
    sender.send_messages("192.168.1.1", 80, ["Hello", "World"])
