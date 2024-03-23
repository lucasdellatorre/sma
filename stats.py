class Stats:
    def __init__(self, queue):
        self.queue = queue

    def calc_prob_distribution(self):
        distribution = [0] * (self.queue.capacity + 1)
        states = self.queue.states
        global_time = self.queue.global_time

        for index, state in enumerate(states):
            distribution[index] = (index, state, state/global_time)

        return distribution

    def show_prob_distribution(self):
        distribution = self.calc_prob_distribution()

        print("Estado\tTempo\tProbabilidade")

        for row in distribution:
            print(f"{row[0]}\t{round(row[1], 1)}\t{row[2] * 100:,.2f}%")
     