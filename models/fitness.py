class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def route_distance(self):
        if self.distance == 0:
            path_distance = 0
            for i in range(0, len(self.route)):
                from_district = self.route[i]
                to_district = None
                if i + 1 < len(self.route):
                    to_district = self.route[i + 1]
                else:
                    to_district = self.route[0]
                path_distance += from_district.distance(to_district)
            self.distance = path_distance
        return self.distance

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness
