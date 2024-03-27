from event import Event, EventType
from scheduler import Scheduler
from queue_1 import Queue

class Simulation:
    def __init__(self, arrival, queue: Queue, scheduler: Scheduler):
        self.arrival = arrival
        self.queue = queue
        self.scheduler = scheduler

    def run(self):
        self.scheduler.add_rand(Event(EventType.ARRIVE, self.arrival), 0)

        while self.scheduler.random_numbers.current != self.scheduler.random_numbers.total_numbers:
            next_event = self.scheduler.schedule()

            if next_event == None:
                break

            if (next_event.type == EventType.ARRIVE):
                self.queue.arrival(next_event)
            elif (next_event.type == EventType.EXIT):
                self.queue.exit(next_event)
