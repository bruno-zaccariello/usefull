import string
from Classes.my_exceptions import UserError

class Graph(object):
    def __init__(self, graph_dict={}, graph_list=[]):
        if graph_dict:
            self.set_graph(graph_dict=graph_dict)
        elif graph_list:
            self.set_graph(graph_list=graph_list)

    def set_graph(self, graph_dict={}, graph_list=[]):
        if graph_dict:
            self._graph_dict = graph_dict
        elif graph_list:
            self._graph_dict = self.gen_dict(graph_list)

    def gen_dict(self, graph):
        tmp = string.ascii_lowercase
        _dict = {}
        for node in range(len(graph)):
            _dict[tmp[node]] = []
            for each in range(len(graph[node])):
                if graph[node][each] == 1:
                    _dict[tmp[node]].append(tmp[each])
        return _dict

    def add_nodes(self, nodes=[]):
        for node in nodes:
            if node not in self._graph_dict:
                self._graph_dict[node] = []
            else:
                continue
        return self

    def add_paths(self, node, paths=[], both_ways=True):
        graph = self._graph_dict
        if node in graph.keys():
            for path in paths:
                if path in graph.keys():
                    if path not in graph[node]:
                        graph[node].append(path)
                if node not in graph[path] and both_ways:
                    graph[path].append(node)
                else:
                    print('Path not valid or already exists\nskipping...')
        return self


    def get_nodes(self):
        vals = list(self._graph_dict.keys())
        return vals

    def get_paths(self, node):
        if node in self.get_nodes():
            graph = dict(self._graph_dict)
            return graph[node]
        else:
            raise UserError(f'''This node is not contained in this Graph
                    Avaible nodes: {self.get_nodes()}''')


    def get_distance(self, node1, node2):
        if node1 in self.get_nodes() and node2 in self.get_nodes():
            distances = {}
            distances[node1] = 0
            q = []  # Queue
            q.append(node1)
            while len(q) > 0:
                actual = q.pop(0)
                actual_paths = self.get_paths(actual)
                for path in actual_paths:
                    if path not in distances:
                        distances[path] = distances[actual] + 1
                        q.append(path)
            return distances.get(node2, 'One or other isolated node')
        else:
            raise UserError(f'''One node is not contained in this Graph
                    Avaible nodes: {self.get_nodes()}''')

def examples():
    try_it = {"a": ["d", "f"],
              "b": ["c"],
              "c": ["b", "c", "d", "e"],
              "d": ["a", "c"],
              "e": ["c"],
              "f": ["d"]
              }
    graph = Graph(try_it)
    graph.add_nodes(['g', 'h', 'z'])
    graph.add_paths('g',['a','d','c'])
    graph.add_paths('h',['z'])
    graph.add_paths('z', ['a'], False)
    print(graph.get_paths('a'))
    print(graph.get_paths('h'))
    print(graph.get_paths('z'))
    print(graph.get_distance('h','a'))
    print(graph.get_distance('a','h'))
