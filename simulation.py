from event import Event, EventType
from scheduler import Scheduler
from queue_1 import Queue
from interval import Interval

class Simulation:
    def __init__(self, arrival_time, queues, scheduler):
        self.arrival_time = arrival_time
        self.queues = queues
        self.scheduler = scheduler
        self.global_time = 0

    def run(self):
        first_queue = self.queues[0]
        self.scheduler.add_rand(Event(EventType.ARRIVE, self.arrival_time, None, first_queue), 0)
        while (self.scheduler.random_numbers.current + 2) <= self.scheduler.random_numbers.total_numbers: # tem que colocar +2 pq o current comeca com -1 
            next_event = self.scheduler.schedule()
            
            self.__update_global_time(next_event)

            if (next_event.type == EventType.ARRIVE):
                self.arrival(None, next_event.target)
            elif (next_event.type == EventType.EXIT):
                self.exit(next_event.source, None)
            elif (next_event.type == EventType.MOVE):
                self.move(next_event.source, next_event.target)
        
    def arrival(self, _, target: Queue):
        if target.status < target.capacity:
            target.add()
            if target.status <= target.servers:
                event = target.target(self.scheduler.get_random(Interval(0, 1)), self.global_time)
                self.scheduler.add(event, target.service_interval)
        else:
            target.loss()
        self.scheduler.add(Event(EventType.ARRIVE, self.global_time, None, target), target.arrival_interval)

    def exit(self, source, _):
        source.out()
        if source.status >= source.servers:
            self.scheduler.add(source.target(self.scheduler.get_random(Interval(0, 1)), self.global_time), source.service_interval)
            
    def move(self, source, target):
        source.out()
        if source.status >= source.servers:
            self.scheduler.add(source.target(self.scheduler.get_random(Interval(0, 1)), self.global_time), source.service_interval)
        if target.status < target.capacity:
            target.add()
            if target.status <= target.servers:
                self.scheduler.add(target.target(self.scheduler.get_random(Interval(0, 1)), self.global_time), target.service_interval)
        else:
            target.loss()

    def __update_global_time(self, event):
        for queue in self.queues:
            queue.update_states(event.time - self.global_time)
        self.global_time = event.time