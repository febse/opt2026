
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import numpy as np

# Създаваме нов ориентиран граф
G = nx.DiGraph()

# Добавяме възли с координати
positions = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (2, 1),
    'D': (3, 3),
    'E': (4, 1),
    'F': (5, 2),
    'T': (6, 0),
    'H': (2, -1),
    'I': (4, -1),
    'J': (5, 3)
}

# Добавяме дъги с тегла
edges = [
    ('A', 'B', 9, 2, 0.001),
    ('A', 'C', 14, 3, 0.002),
    ('B', 'D', 7, 4, 0.003),
    ('C', 'D', 16, 1, 0.001),
    ('C', 'E', 20, 5, 0.001),
    ('D', 'F', 18, 2, 0.005),
    ('E', 'F', 10, 3, 0.002),
    ('F', 'T', 11, 1, 0.010),
    ('A', 'H', 23, 4, 0.008),
    ('H', 'C', 13, 2, 0.006),
    ('H', 'I', 12, 3, 0.002),
    ('I', 'E', 15, 2, 0.001),
    ('I', 'T', 25, 4, 0.002),
    ('D', 'J', 24, 3, 0.002),
    ('J', 'F', 18, 2, 0.008)
]

# Добавяме дъгите в графа
for u, v, c, w, prob in edges:
    G.add_edge(u, v, Capacity=c, Distance=w, Probability=prob)


def fmt_flow(value: float) -> str:
    return str(int(round(value))) if abs(value - round(value)) < 1e-9 else f"{value:.2f}"


def visualize_graph(edge_attribute: str, title: str, edge_labels: dict | None = None, edge_label_color: str = 'black'):

    if edge_attribute not in G.edges[next(iter(G.edges))]:
        raise ValueError(
            f"Графът няма атрибут '{edge_attribute}' за дъгите. Моля, изберете валиден атрибут от {list(G.edges[next(iter(G.edges))].keys())}.")

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos=positions, with_labels=True, node_size=700,
            node_color='lightblue', font_size=10, font_weight='bold', arrows=True)

    # Етикетите на дъгите
    if edge_labels is None:
        edge_labels = nx.get_edge_attributes(G, edge_attribute)
    nx.draw_networkx_edge_labels(
        G, pos=positions, edge_labels=edge_labels, rotate=False, font_color=edge_label_color)

    for node, (x, y) in positions.items():
        circle = mpatches.Circle(
            (x, y), radius=0.2, color='lightblue', alpha=0.5)
        plt.gca().add_patch(circle)

    plt.xlim(-1, 7)
    plt.ylim(-2, 5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.grid()
    plt.show()
