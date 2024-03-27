from event import Event, EventType

class Simulation:
    def __init__(self, arrival, queue, scheduler):
        self.arrival = arrival
        self.queue = queue
        self.scheduler = scheduler

    def run(self):
        self.scheduler.add_rand(Event(EventType.ARRIVE, self.arrival), 0)

        while len(self.scheduler.random_numbers) != 0:
            next_event = self.scheduler.schedule()

            if next_event == None:
                break

            if (next_event.type == EventType.ARRIVE):
                self.queue.arrival(next_event)
            elif (next_event.type == EventType.EXIT):
                self.queue.exit(next_event)
