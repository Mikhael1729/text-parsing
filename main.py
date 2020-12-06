from representation import Graph

words = [
  "Para",
  "De",
  "Uno",
  "La",
  "Es",
  "Luna",
  "Sol",
  "Carro",
  "Hola",
  "Arbol",
  "Silla",
  "Mesa",
  "Casa",
  "Año",
  "Rio",
  "Mesa",
  "Perro",
  "Calle",
  "Feliz",
  "Son"
]

def connect(word, graph):
  concatenation = ""
  for i in range(0, len(word) - 1): # para
    letter = word[i]
    next_letter = word[i + 1]

    concatenation += letter

    n1 = graph.add_node(concatenation) # p

    concatenation += next_letter

    n2 = graph.add_node(concatenation)

    if i > 0:
      graph.add_edge(n1.id, n2.id, letter)

def generate_states_space():
  S = Graph()

  for word in words:
    connect(word, S)

  return S

states_space = generate_states_space()

for key, value in states_space.nodes.items():
  print(value)

