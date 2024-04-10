import yaml
from sys import argv
from interval import Interval
from queue_1 import Queue
from scheduler import Scheduler
from simulation import Simulation
from stats import Stats
from pseudo_random_numbers import PseudoRandomNumbers

CONFIG = {}

def load_config(file_name):
    global CONFIG

    with open(file_name) as stream:
        try:
            CONFIG = yaml.safe_load(stream)
        except:
            print('=== ERROR LOADING YAML FILE ===')
            exit(0)

def initialize_queue(config, queue_name) -> Queue:
    queue_config = config['queues'][queue_name]

    capacity = queue_config['capacity']
    servers = queue_config['servers']
    service_interval = Interval(queue_config['minService'], queue_config['maxService'])

    if queue_name == 'Q1':
        arrival_interval = Interval(queue_config['minArrival'], queue_config['maxArrival'])
    else:
        arrival_interval = None

    return Queue(capacity=capacity, servers=servers, arrival_interval=arrival_interval, service_interval=service_interval)

def main():
    global CONFIG

    load_config(argv[1])

    arrival_time = CONFIG['arrivals']['Q1']
    seeds = CONFIG['seed']
    q1 = initialize_queue(CONFIG, 'Q1')
    q2 = initialize_queue(CONFIG, 'Q2')
    total_rnd_numbers = CONFIG['rndnumbersPerSeed']
    random_numbers = CONFIG.get('rndnumbers')
      
    random_numbers = PseudoRandomNumbers(seeds[0], total_rnd_numbers, random_numbers=random_numbers, generate=not bool(random_numbers))
    
    scheduler = Scheduler(random_numbers)

    sim = Simulation(arrival_time=arrival_time, queue1=q1, queue2=q2, scheduler=scheduler)

    sim.run()

    Stats(sim).report()

if __name__ == '__main__':
    main()
