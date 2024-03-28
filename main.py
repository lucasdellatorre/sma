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

    SEED = CONFIG['seed']
    q1_config = CONFIG['queues']['q1']

    ARRIVAL_TIME = q1_config['arrivalTime']
    Q1_CAPACITY = q1_config['capacity']
    Q1_SERVERS = q1_config['servers']
    Q1_ARRIVAL_INTERVAL = Interval(q1_config['minArrival'], q1_config['maxArrival'])
    Q1_SERVICE_INTERVAL = Interval(q1_config['minService'], q1_config['maxService'])

    q1 = Queue(capacity=Q1_CAPACITY, servers=Q1_SERVERS, arrival_interval=Q1_ARRIVAL_INTERVAL, service_interval=Q1_SERVICE_INTERVAL)

    q2_config = CONFIG['queues']['q2']

    Q2_CAPACITY = q2_config['capacity']
    Q2_SERVERS = q2_config['servers']
    Q2_ARRIVAL_INTERVAL = Interval(q2_config['minArrival'], q2_config['maxArrival'])
    Q2_SERVICE_INTERVAL = Interval(q2_config['minService'], q2_config['maxService'])

    q2 = Queue(capacity=Q2_CAPACITY, servers=Q2_SERVERS, arrival_interval=Q2_ARRIVAL_INTERVAL, service_interval=Q2_SERVICE_INTERVAL)

    random_numbers = (
        PseudoRandomNumbers(SEED).gen_rand(CONFIG['qntRandomNumbers']) 
        if not CONFIG.get('randomNumbers') or CONFIG.get('generateRandonNumbers') 
        else CONFIG['randomNumbers']
    )

    SCHEDULER = Scheduler(random_numbers)

    print(q1_config)
    print(q2_config)

    print(q1)
    print(q2)

    sim = Simulation(arrival_time=ARRIVAL_TIME, queue1=q1, queue2=q2, scheduler=SCHEDULER)

    sim.run()

    stats = Stats(sim)

    stats.show_prob_distribution()

    stats.show_losses(q1)
    stats.show_losses(q2)

    stats.show_global_time()


if __name__ == '__main__':
    main()
