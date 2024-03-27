from interval import Interval
from queue_1 import Queue
from scheduler import Scheduler
from simulation import Simulation
from stats import Stats
from pseudo_random_numbers import PseudoRandomNumbers
from sys import argv
import yaml


CONFIG = {}

def load_config(file_name):
    global CONFIG

    with open(file_name) as stream:
        try:
            CONFIG = yaml.safe_load(stream)
        except:
            print('=== ERROR LOADING YAML FILE ===')
            exit(0)


def main():
    global CONFIG

    load_config(argv[1])

    ARRIVAL_TIME = CONFIG['arrivalTime']
    CAPACITY = CONFIG['capacity']
    SERVERS = CONFIG['servers']
    ARRIVAL_INTERVAL = Interval(CONFIG['minArrival'], CONFIG['maxArrival'])
    SERVICE_INTERVAL = Interval(CONFIG['minService'], CONFIG['maxService'])

    SEED = CONFIG['seed']
    

    random_numbers = PseudoRandomNumbers(SEED, CONFIG['qntRandomNumbers'], random_numbers=CONFIG.get('randomNumbers'), generate=CONFIG.get('generateRandonNumbers')) 
    
    SCHEDULER = Scheduler(random_numbers)
    

    queue = Queue(capacity=CAPACITY, servers=SERVERS, scheduler=SCHEDULER, arrival_interval=ARRIVAL_INTERVAL, service_interval=SERVICE_INTERVAL)

    sim = Simulation(arrival=ARRIVAL_TIME, queue=queue, scheduler=SCHEDULER)

    sim.run()

    stats = Stats(queue)

    stats.show_prob_distribution()

    stats.show_losses()

    stats.show_global_time()


if __name__ == '__main__':
    main()
