from event import Event, EventType

class Simulation:
    def __init__(self, arrival_time, queue1, queue2, scheduler):
        self.arrival_time = arrival_time
        self.queue1 = queue1
        self.queue2 = queue2
        self.scheduler = scheduler
        self.global_time = 0

    def run(self):
        self.scheduler.add_rand(Event(EventType.ARRIVE, self.arrival_time), 0)
        while len(self.scheduler.random_numbers) != 0:
            next_event = self.scheduler.schedule()
            print("-----")
            print(next_event)
            print('randomNumbers', self.scheduler.random_numbers)

            if (next_event.type == EventType.ARRIVE):
                self.arrival(next_event)
            elif (next_event.type == EventType.EXIT):
                self.exit(next_event)
            elif (next_event.type == EventType.MOVE):
                self.move(next_event)
            count = count - 1
        
    def arrival(self, event):
        self.__update_global_time(event)
        if self.queue1.status < self.queue1.capacity:
            self.queue1.add()
            if self.queue1.status <= self.queue1.servers:
                self.scheduler.add(Event(EventType.MOVE, self.global_time), self.queue1.service_interval)
        else:
            self.queue1.loss()
        self.scheduler.add(Event(EventType.ARRIVE, self.global_time), self.queue1.arrival_interval)

    def exit(self, event):
        print("exit", event)
        self.__update_global_time(event)
        self.queue2.out()
        if self.queue2.status >= self.queue2.servers:
            self.scheduler.add(Event(EventType.EXIT, self.global_time), self.queue2.service_interval)

    def move(self, event):
        self.__update_global_time(event)
        print("passagem", event)
        self.queue1.out()
        if self.queue1.status >= self.queue1.servers:
            self.scheduler.add(Event(EventType.MOVE, self.global_time), self.queue1.service_interval)
        if self.queue2.status < self.queue2.capacity:
            self.queue2.add()
            if self.queue2.status <= self.queue2.servers:
                self.scheduler.add(Event(EventType.EXIT, self.global_time), self.queue2.service_interval)
        else:
            self.queue2.loss()

    def __update_global_time(self, event):
        self.queue1.update_states(event.time - self.global_time)
        self.queue2.update_states(event.time - self.global_time)
        self.global_time = event.time
        print(self.queue1.states)
        print("queue2states", self.queue2.states)