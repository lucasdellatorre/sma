class Stats:
    def __init__(self, simulation):
        self.simulation = simulation 

    def calc_prob_distribution(self, queue):
        distribution = [0] * (queue.capacity + 1)
        states = queue.states
        global_time = self.simulation.global_time

        for index, state in enumerate(states):
            distribution[index] = (index, state, state/global_time)

        return distribution

    def show_prob_distribution(self, queue):
        distribution = self.calc_prob_distribution(queue)

        print("State\t\tTime\t\tProbability")
        for row in distribution:
            if row[1] != 0:
                print(f"{row[0]}\t\t{round(row[1], 4)}\t\t{row[2] * 100:,.2f}%")

    def show_global_time(self):
        print("Simulation average time:", self.simulation.global_time)

    def show_losses(self, queue):
        print("Number of losses:", queue.losses)
    
    def report(self):
        for index, queue in enumerate(self.simulation.queues): 
            k = queue.capacity
            print("***********************************************************")
            if not k == 100:
                print(f"Queue:   Q{index+1} (G/G/{queue.servers}/{queue.capacity})")
            else:
                print(f"Queue:   Q{index+1} (G/G/{queue.servers})")
            if queue.arrival_interval != None:
                print(f"Arrival: {queue.arrival_interval.start} ... {queue.arrival_interval.end}")
            print(f"Service: {queue.service_interval.start} ... {queue.service_interval.end}")
            print("***********************************************************")
            self.show_prob_distribution(queue)
            self.show_losses(queue)

        self.show_global_time()


     
