from enum import Enum

class EventType(Enum):
    ARRIVE = 'arrive'
    EXIT = 'exit'
    MOVE = 'move'

class Event:
    def __init__(self, type, time) -> None:
        self.type = type
        self.time = time

    def __str__(self):
        return f'Type:{self.type} | Time: {self.time}'



