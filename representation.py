import pprint
from collections import defaultdict

class Node:
  """
  id: Unique value to identify the node
  value: the letter o word
  adjacents: linked list of edges
  """
  def __init__(self, id, value=None, adjacents=[]):
    self.id = id
    self.value = value 
    self.adjacents = adjacents

  def __str__(self):
    return f"Node(id: {self.id}, value: {self.value})"

class Edge:
  """
  value: Symbol of the transition
  source: Node source
  destination Node destination
  """
  def __init__(self, id, value, source, destination):
    self.id = id
    self.value = value
    self.source = source
    self.destination = destination

  def __str__(self):
    return f"Edge(id: {self.id}, value: {self.value}, source: {self.source}, destination: {self.destination})"

class Graph:
  def __init__(self, directed=True):
    self.nodes = {} # Nodes dictionary.
    self.edges = [] # List of edges.
    self.directed = False

  def add_node(self, value):
    new_id = self.__generate_next_node_id()
    self.nodes[new_id] = Node(id, value=value)

  def __generate_next_node_id(self):
    new_id = len(self.nodes)
    return new_id

  def add_edge(self, source_id, destination_id, value):
    edge = Edge(
      id = self.__generate_next_edge_id(),
      value = value,
      source = source_id,
      destination = destination_id
    )

    self.edges.append(edge)

    self.nodes[source_id].adjacents.append(edge)

    if not self.directed:
      self.nodes[destination_id].adjacents.append(edge)

  def __generate_next_edge_id(self):
    last_edge = self.edges[-1]
    return last_edge.id + 1 if last_edge else 0

  def get_node(self, id):
    node_exists = True if id >= 0 and id < len(self.nodes) else False
    if node_exists:
      return self.nodes[id]
    else:
      print("NODE DOESN'T EXISTS")
      return None

