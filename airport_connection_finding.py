airport = [
    "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
    "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]

route = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]]

start = "DSM"


class Airport:

    def __init__(self, name, airports=airport, routes=route.copy()):
        self.Connections = [name]
        self.MissingAirports = airports.copy()
        self.MissingAirports.remove(name)

        for i in routes:
            if i[0] == name and i[1] not in self.Connections:
                self.Connections.append(i[1])
                self.MissingAirports.remove(i[1])

        for i in self.Connections:
            for j in routes:
                if j[0] == i and j[1] not in self.Connections:
                    self.Connections.append(j[1])
                    self.MissingAirports.remove(j[1])

    def count_new_connection(self, name):
        new_airport = Airport(name)
        connections = self.Connections.copy()
        count_0 = 0
        for i in new_airport.Connections:
            if i not in connections:
                count_0 += 1
        return count_0

    def connect_to(self, name):
        new_airport = Airport(name)
        for i in new_airport.Connections:
            if i not in self.Connections:
                self.Connections.append(i)
                self.MissingAirports.remove(i)


start = Airport(start)

iterations = 0
while len(start.Connections) != len(airport):
    count = [start.count_new_connection(i) for i in start.MissingAirports]
    start.connect_to(start.MissingAirports[count.index(max(count))])
    iterations += 1

print(iterations)
