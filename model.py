from enums import SonicareValueType

class Service:
    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics

class ReadWriteNotify():
    def __init__(self, read, write, notify):
        self.read = read
        self.write = write
        self.notify = notify

class Characteristic:
    def __init__(self, name, readwritenotify, data_type=SonicareValueType.RAW, enum=None):
        self.name = name
        self.data_type = data_type
        self.enum = enum
        self.readWriteNotify = readwritenotify
    
