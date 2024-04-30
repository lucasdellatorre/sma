import yaml
from sys import argv
from interval import Interval
from queue_1 import Queue
from scheduler import Scheduler
from simulation import Simulation
from stats import Stats
from pseudo_random_numbers import PseudoRandomNumbers

def load_config(file_name):
    with open(file_name) as stream:
        try:
            CONFIG = yaml.safe_load(stream)
        except:
            print('=== ERROR LOADING YAML FILE ===')
            exit(0)

    return CONFIG

def get_queues(config) -> list:
    queues_config = config['queues']

    queues = []

    for _, queue_id in enumerate(queues_config):
        queue_config = queues_config[queue_id]

        servers = queue_config['servers']
        service_interval = Interval(queue_config['minService'], queue_config['maxService'])

        if "capacity" in queue_config:
            capacity = queue_config['capacity']
        else:
            capacity = 100 ## preguica de fazer um jeito melhor, mas o certo seria colocar um valor -1 aqui e tratar nos outros lugares do codigo

        if "minArrival" in queue_config:
            arrival_interval = Interval(queue_config['minArrival'], queue_config['maxArrival'])
        else:
            arrival_interval = None
            
        queues.append(Queue(capacity=capacity, id=queue_id, servers=servers, arrival_interval=arrival_interval, service_interval=service_interval))
    
    return queues

# not used
def get_backbone(config, queue_size) -> list:
    network = config["network"]
    backbone = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    for event in network:
        source = event["source"]
        target = event["target"]
        probability = event["probability"]
        s = int(source[1:])
        t = int(target[1:])
        backbone[s][t] = float(probability)

    # verifica a probabilidade para fila de saida
    for queue_events in backbone:
        sum_prob = sum(queue_events)
        if sum_prob != 1:
            queue_events[0] = round(1 - sum_prob, 1)

    return backbone

def add_network(source_id, target_id, prob, queues: list):
    source: Queue = queues[int(source_id[1:]) - 1]
    target: Queue = queues[int(target_id[1:]) - 1]
    source.add_queue(target, prob)

def main():
    CONFIG = load_config(argv[1])

    arrival_time = CONFIG['arrivals']['Q1']

    seeds = CONFIG['seed']
    
    queues = get_queues(CONFIG)
    
    network = CONFIG["network"]
    
    for event in network:
        add_network(event["source"], event["target"], event["probability"], queues)
        
    total_rnd_numbers = CONFIG['rndnumbersPerSeed']

    random_numbers = CONFIG.get('rndnumbers')
      
    random_numbers = PseudoRandomNumbers(seeds[0], total_rnd_numbers, random_numbers=random_numbers, generate=not bool(random_numbers))
    
    scheduler = Scheduler(random_numbers)

    sim = Simulation(arrival_time=arrival_time, queues=queues, scheduler=scheduler)

    sim.run()

    Stats(sim).report()

if __name__ == '__main__':
    main()
