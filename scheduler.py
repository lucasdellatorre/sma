from event import Event
from pseudo_random_numbers import PseudoRandomNumbers

class Scheduler():
    def __init__(self, random_numbers: PseudoRandomNumbers):
        self.random_numbers = random_numbers
        self.scheduler = []

    def add(self, event, interval):
        if self.random_numbers.current == self.random_numbers.total_numbers:
            return
        event.time = event.time + self.get_random(interval)
        self.scheduler.append(event)
        self.scheduler.sort(key=lambda event: event.time)

    def add_rand(self, event, rand_num):
        event.time = event.time + rand_num
        self.scheduler.append(event)
        self.scheduler.sort(key=lambda event: event.time)

    def schedule(self) -> Event:
        return self.scheduler.pop(0)
    
    def get_random(self, interval) -> float:
        rand_num = self.random_numbers.get_next_number()
        return interval.start + (interval.end - interval.start) * rand_num




