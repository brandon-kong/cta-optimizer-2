from typing import List
from networkx import DiGraph, shortest_path

from cta_optimizer.models.station import Station


class StationsGraphService:
    def __init__(self):
        self.graph = DiGraph()

    def add_station(self, station: Station):
        if station is None:
            raise ValueError("Invalid station")

        self.graph.add_node(station)

    def add_edge(self, station1: Station, station2: Station):
        if station1 not in self.graph.nodes() or station2 not in self.graph.nodes():
            raise ValueError("Invalid station")

        # Make sure that both stations are not the same and are not closed
        if station1 == station2 or station1.is_closed() or station2.is_closed():
            return

        distance = station1.get_location().distance_to(station2.get_location())
        self.graph.add_weighted_edges_from(
            [(station1, station2, distance.value)], "distance"
        )

    def get_adjacent_stations(self, station: Station):
        if station not in self.graph.nodes():
            raise ValueError("Invalid station")

        return self.graph.adj[station]

    def get_all_stations(self):
        return self.graph.nodes()

    def get_shortest_path(self, start: Station, end: Station) -> List[Station]:
        if start is None:
            raise ValueError("Start station cannot be None")

        if end is None:
            raise ValueError("End station cannot be None")

        if start not in self.graph.nodes() or end not in self.graph.nodes():
            raise ValueError("Invalid station")

        return list(shortest_path(self.graph, start, end, weight="distance"))
