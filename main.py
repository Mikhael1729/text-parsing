from representation import Graph
from representation import heuristic
from representation import KEY_WORDS
# words = [
#   "para",
#   "de",
#   "uno",
#   "la",
#   "es",
#   "luna",
#   "sol",
#   "carro",
#   "hola",
#   "arbol",
#   "silla",
#   "mesa",
#   "casa",
#   "año",
#   "rio",
#   "mesa",
#   "perro",
#   "calle",
#   "feliz",
#   "son"
# ]

# S = Graph()
# s1 = S.add_node("p")
# s2 = S.add_node("pa")
# s3 = S.add_node("par")
# s4 = S.add_node("para")

# S.add_edge(s1.id, s2.id, "a")
# S.add_edge(s2.id, s3.id, "r")
# S.add_edge(s3.id, s4.id, "a")

def connect2(word, graph):
  nodes = []
  concatenation = ""
  
  # Add nodes
  for letter in word:
    concatenation += letter
    nodes.append(graph.add_node(concatenation))

  # Add edges
  for i in range(1, len(word)):
    letter = word[i]
    graph.add_edge(nodes[i - 1].id, nodes[i].id, letter)


def generate_states_space2():
  S = Graph()

  for word in KEY_WORDS:
    connect2(word, S)

  return S

generated = generate_states_space2()
for key, value in generated.nodes.items():
#   print(value)
    continue

def bfs(graph, goal_word):
    open_l = []
    closed_l = []
    not_modified_open = []
    not_modified_closed = []

    open_l.append(graph.nodes[0])
    not_modified_open.append(graph.nodes[0])
    times = 0

    while True:
        if len(open_l) == 0:
            return False
        
        min_h = 10
        min_n = open_l[0]
        # gets the node with the lowest value of h(n)
        for node in open_l:
            current_h = heuristic(node)
            if current_h < min_h:
                min_h = current_h
                min_n = node
                # print(min_n)

        open_l.remove(min_n)
        closed_l.append(min_n)
        not_modified_closed.append(min_n)

        # check if any successor is goal node or not
        childs = min_n.adjacents
        for child in childs:
            if child.destination.value == goal_word:
                return True

        for child in childs:
            if child not in not_modified_open and child not in not_modified_closed:
                open_l.append(child.destination)
                not_modified_open.append(child.destination)

        times += 1
        if times > len(graph.edges):
            return False

text = "Uno De Hola Denys Mikhael Erica Luna"

for word in text.split(" "):
    print(word + ': ' + str(bfs(generated, word)))
