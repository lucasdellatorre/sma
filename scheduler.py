from event import Event

class Scheduler():
    def __init__(self, random_numbers):
        self.random_numbers = random_numbers
        self.scheduler = []

    def add(self, event, interval):
        if len(self.random_numbers) == 0:
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
        rand_num = self.random_numbers.pop(0)
        return interval.start + (interval.end - interval.start) * rand_num




