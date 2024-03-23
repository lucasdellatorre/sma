from interval import Interval
from queue_1 import Queue
from scheduler import Scheduler
from simulation import Simulation

arrival_time = 1
capacity = 4 
servers = 1
random_numbers = [0.8, 0.2, 0.1, 0.9, 0.3, 0.4, 0.7]
scheduler = Scheduler(random_numbers)
arrival_interval = Interval(1,2)
service_interval = Interval(2,3)

queue = Queue(capacity=capacity, servers=servers, scheduler=scheduler,arrival_interval=arrival_interval, service_interval=service_interval)

sim = Simulation(arrival=arrival_time, queue=queue, scheduler=scheduler, random_numbers=random_numbers)

sim.run()
