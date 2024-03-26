from interval import Interval
from queue_1 import Queue
from scheduler import Scheduler
from simulation import Simulation
from stats import Stats

arrival_time = 2
capacity = 5
servers = 3
random_numbers = [0.8, 0.2, 0.1, 0.9, 0.3, 0.4, 0.7]
scheduler = Scheduler(random_numbers)
arrival_interval = Interval(2,5)
service_interval = Interval(3,5)

queue = Queue(capacity=capacity, servers=servers, scheduler=scheduler,arrival_interval=arrival_interval, service_interval=service_interval)

sim = Simulation(arrival=arrival_time, queue=queue, scheduler=scheduler, random_numbers=random_numbers)

sim.run()

stats = Stats(queue)

stats.show_prob_distribution()

stats.show_losses()

stats.show_global_time()