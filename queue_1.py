class Queue:
    def __init__(self, capacity, servers, arrival_interval, service_interval) -> None:
        self.capacity = capacity 
        self.servers = servers
        self.arrival_interval = arrival_interval
        self.service_interval = service_interval
        self.status = 0
        self.losses = 0
        self.states = [0] * (capacity + 1)

    def add(self):
        self.status = self.status + 1

    def out(self):
        self.status = self.status - 1

    def loss(self):
        self.losses = self.losses + 1

    def update_states(self, time):
        self.states[self.status] = self.states[self.status] + time 


    def __str__(self) -> str:
        string = f'Capacity: {self.capacity}' + '\n'
        string = string + f'Servers: {self.servers}' + '\n'
        string = string + f'Arrival Interval: {self.arrival_interval}' + '\n'
        string = string + f'Service Interval: {self.service_interval}' + '\n'
        string = string + f'Status: {self.status}' + '\n'
        string = string + f'Losses: {self.losses}' + '\n'
        string = string + f'States: {self.states}'

        return string

