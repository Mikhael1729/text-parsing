from representation import Graph

words = [
  "para",
  "de",
  "uno",
  "la",
  "es",
  "luna",
  "sol",
  "carro",
  "hola",
  "arbol",
  "silla",
  "mesa",
  "casa",
  "año",
  "rio",
  "mesa",
  "perro",
  "calle",
  "feliz",
  "son"
]

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

  for word in words:
    connect2(word, S)

  return S

generated = generate_states_space2()
for key, value in generated.nodes.items():
  print(value)
