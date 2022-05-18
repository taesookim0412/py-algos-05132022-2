# dijkstra's TLE

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for flight in flights:
            frm, to, price = flight
            if frm not in graph:
                graph[frm] = {}
            graph[frm][to] = price
        # print(graph)
        # [[dest_price, location, stop_ctr]]
        pq = [[0, src, 0]]
        while pq:
            flight_data = heapq.heappop(pq)
            dest_price, location, stop_ctr = flight_data
            # print(flight_data)
            if stop_ctr - 1 <= k:
                if location == dst:
                    return dest_price
                if location in graph:
                    for graph_dest, graph_additional_cost in graph[location].items():
                        heapq.heappush(pq, [dest_price + graph_additional_cost, graph_dest, stop_ctr + 1])
        return -1