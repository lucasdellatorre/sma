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

    def show_prob_distribution(self):
        q1 = self.simulation.queue1
        q2 = self.simulation.queue2
        distribution1 = self.calc_prob_distribution(q1)
        distribution2 = self.calc_prob_distribution(q2)

        print("State\tTime\tProbability")

        print("Queue1")
        for row in distribution1:
            print(f"{row[0]}\t{round(row[1], 1)}\t{row[2] * 100:,.2f}%")

        print("Queue2")
        for row in distribution2:
            print(f"{row[0]}\t{round(row[1], 1)}\t{row[2] * 100:,.2f}%")

    def show_global_time(self):
        print("Simulation average time:", self.simulation.global_time)

    def show_losses(self, queue):
        print("Number of losses:", queue.losses)
     
