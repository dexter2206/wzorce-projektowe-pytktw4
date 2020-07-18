class Url:
    def __init__(self, address, protocol="http", port=80):
        self.address = address
        self.protocol = protocol
        self.port = port

    @classmethod
    def from_string(cls, url_string: str):
        parts = url_string.split("://")
        protocol = "http" if len(parts) == 1 else parts[0]
        parts = parts[-1].split(":")
        port = 80 if len(parts) == 1 else parts[1]
        return cls(parts[0], protocol=protocol, port=port)

    @classmethod
    def from_string2(cls, url_string: str):
        kwargs = {}
        parts = url_string.split("://")
        if len(parts) == 2:
            kwargs["protocol"] = parts[0]
        parts = parts[-1].split(":")
        if len(parts) == 2:
            kwargs["port"] = parts[1]

        return cls(parts[0], **kwargs)

    def __str__(self):
        return f"{self.protocol}://{self.address}:{self.port}"


if __name__ == '__main__':
    google_url = Url.from_string("www.google.com")
    print(google_url.protocol)
    print(google_url.address)
    print(google_url.port)
