from enum import Enum

class EventType(Enum):
    ARRIVE = 'arrive'
    EXIT = 'exit'
    MOVE = 'move'

class Event:
    def __init__(self, type, time, source, target) -> None:
        self.type = type
        self.time = time
        self.source = source
        self.target = target

    def __str__(self):
        return f'Type:{self.type} | Time: {self.time} | Source: {self.source} | Target: {self.target}'



