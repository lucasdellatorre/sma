from event import Event, EventType

class Queue:
    def __init__(self, capacity, servers, scheduler, arrival_interval, service_interval) -> None:
        self.capacity = capacity 
        self.servers = servers
        self.scheduler = scheduler 
        self.arrival_interval = arrival_interval
        self.service_interval = service_interval
        self.global_time = 0
        self.status = 0
        self.losses = 0
        self.states = [0] * (capacity + 1)

    def arrival(self, event):
        self.__update_global_time(event)
        if self.status < self.capacity:
            self.status = self.status + 1
            if self.status <= self.servers:
                self.scheduler.add(Event(EventType.EXIT, self.global_time), self.service_interval)
        else:
            self.losses = self.losses + 1
        self.scheduler.add(Event(EventType.ARRIVE, self.global_time), self.arrival_interval)

    def exit(self, event):
        self.__update_global_time(event)
        self.status = self.status - 1
        if self.status >= self.servers:
            self.scheduler.add(Event(EventType.EXIT, self.global_time), self.service_interval)

    def __update_global_time(self, event):
        self.states[self.status] = self.states[self.status] + event.time - self.global_time 
        self.global_time = event.time